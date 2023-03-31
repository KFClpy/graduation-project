from mysqldb.exts import db
from mysqldb.models import RevokedTokenModel


def is_jti_blacklisted(jti):
    query = db.session.query(RevokedTokenModel).filter(RevokedTokenModel.jti == jti).first()
    return bool(query)


def add_revoked_token(revokedtoken):
    try:
        db.session.add(revokedtoken)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        raise e
