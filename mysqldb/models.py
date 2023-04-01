from werkzeug.security import generate_password_hash, check_password_hash

from mysqldb.exts import db


class User(db.Model):
    __tablename__ = "t_user"
    uid = db.Column(db.Integer, primary_key=True)
    tusername = db.Column(db.String(20), unique=True, nullable=False)
    tpassword = db.Column(db.String(150), unique=True, nullable=False)
    gender = db.Column(db.Integer)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(50))
    avatar = db.Column(db.String(255))
    create_user = db.Column(db.String(20))
    create_time = db.Column(db.DateTime)
    modified_user = db.Column(db.String(20))
    modified_time = db.Column(db.DateTime)
    nickname = db.Column(db.String(50))
    identity = db.Column(db.Integer)

    def set_password(self, password):
        self.tpassword = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.tpassword, password)

    def __repr__(self):
        return "<User %r>" % self.tusername


class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    def __repr__(self):
        return "<User %r>" % self.jti
