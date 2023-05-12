from mysqldb.exts import db
from mysqldb.models import User

roleMapping = {
    "super": 3,
    "admin": 2,
    "user": 1
}


def get_user_list(user_name):
    try:
        user = db.session.query(User).filter(User.tusername == user_name).first()
        users = db.session.query(User).all()
        user_list = []
        for current_user in users:
            if roleMapping[current_user.role] < roleMapping[user.role]:
                user_list.append(current_user)
        result = []
        index = 0
        for current_user in user_list:
            index = index + 1
            current_dict = {"index": index, "userName": current_user.tusername, "gender": current_user.gender,
                            "phone": current_user.phone,
                            "email": current_user.email,
                            "role": current_user.role}
            result.append(current_dict)
    except Exception as e:
        raise e
    return result


def delete_user(user_name):
    try:
        db.session.query(User).filter(User.tusername==user_name).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

