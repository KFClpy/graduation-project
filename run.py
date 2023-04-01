from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api

from app import create_app
from errors import errors
from mysqldb.exts import db
from resource import userController
from service import tokenService

app = create_app()


api = Api(app, errors=errors)
api.add_resource(userController.UserRegistration, '/registration')
api.add_resource(userController.UserLogin, '/login')
api.add_resource(userController.TokenRefresh, '/refresh')
api.add_resource(userController.Test, '/test')
api.add_resource(userController.UserLogoutAccess, '/logoutAccess')
api.add_resource(userController.UserLogoutRefresh, '/loginRefresh')
api.add_resource(userController.ChangePassword,'/changepassword')
api.add_resource(userController.ChangeUserInfo,'/changeuserinfo')
jwt = JWTManager(app)
db.init_app(app)
migrate = Migrate(app, db)
app.app_context().push()


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, decrypted_token):
    jti = decrypted_token['jti']
    return tokenService.is_jti_blacklisted(jti)


if __name__ == "__main__":
    app.run()
