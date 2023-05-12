from werkzeug.security import generate_password_hash, check_password_hash
from mysqldb.exts import db


class User(db.Model):
    __tablename__ = "t_user"
    uid = db.Column(db.Integer, primary_key=True)
    tusername = db.Column(db.String(20), unique=True, nullable=False)
    tpassword = db.Column(db.String(150), unique=True, nullable=False)
    gender = db.Column(db.String(5))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(50))
    avatar = db.Column(db.String(255))
    create_user = db.Column(db.String(20))
    create_time = db.Column(db.DateTime)
    modified_user = db.Column(db.String(20))
    modified_time = db.Column(db.DateTime)
    nickname = db.Column(db.String(50))
    role = db.Column(db.String(50))

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


class DataTableModel(db.Model):
    __tablename__ = 'data'
    tid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), db.ForeignKey("mapping.username"), nullable=False, unique=True)
    dataname = db.Column(db.String(50), db.ForeignKey("mapping.dataname"), nullable=False, unique=True)
    attribute1 = db.Column(db.Integer)
    attribute2 = db.Column(db.String(255))
    attribute3 = db.Column(db.String(255))
    attribute4 = db.Column(db.String(255))
    attribute5 = db.Column(db.String(255))
    attribute6 = db.Column(db.String(255))
    attribute7 = db.Column(db.String(255))
    attribute8 = db.Column(db.String(255))
    attribute9 = db.Column(db.String(255))
    attribute10 = db.Column(db.String(255))
    attribute11 = db.Column(db.String(255))
    attribute12 = db.Column(db.String(255))
    attribute13 = db.Column(db.String(255))
    attribute14 = db.Column(db.String(255))
    attribute15 = db.Column(db.String(255))

    def __repr__(self):
        return "<dataTable %r %r>" % self.username % self.dataname


class DataMappingModel(db.Model):
    __tablename__ = 'mapping'
    username = db.Column(db.String(50), primary_key=True)
    dataname = db.Column(db.String(50), primary_key=True)
    th_id = db.Column(db.Integer, primary_key=True)
    th_name = db.Column(db.String(100))


class PreprocessorModel(db.Model):
    __tablename__ = 'preprocessor_config'
    id = db.Column(db.Integer, primary_key=True)
    preprocessor = db.Column(db.String(50), primary_key=True)


class TokenizerModel(db.Model):
    __tablename__ = 'tokenizer_config'
    id = db.Column(db.Integer, primary_key=True)
    tokenizer = db.Column(db.String(50), primary_key=True)


class DistanceFunctionModel(db.Model):
    __tablename__ = 'distance_function_config'
    id = db.Column(db.Integer, primary_key=True)
    distance_function = db.Column(db.String(50), primary_key=True)
