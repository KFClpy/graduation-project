from exception.DuplicateUserException import DuplicateUser
from exception.NoUserException import NoUser
from exception.WrongPasswordException import WrongPassword
from mysqldb.exts import db
from mysqldb.models import User, RevokedTokenModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt)

from service.tokenService import add_revoked_token


def login_user(user):
    users = db.session.query(User).filter(User.tusername == user.tusername).all()
    if len(users) == 0:
        raise NoUser("该用户不存在")
    if not users[0].check_password(user.tpassword):
        raise WrongPassword("密码错误")
    access_token = create_access_token(user.tusername)
    refresh_token = create_refresh_token(user.tusername)
    return {
        'access_token': access_token,
        'refresh_token': refresh_token
    }


def register_user(user):
    size = db.session.query(User).filter(User.tusername == user.tusername).count()
    if size != 0:
        raise DuplicateUser("该用户已被注册")
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as ex:
        print(ex)
        db.session.rollback()
        raise ex
    return True


def logout(jti):
    revoked_token = RevokedTokenModel(jti=jti)
    add_revoked_token(revoked_token)
    return True