from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api

from app import create_app
from errors import errors
from mysqldb.exts import db
from resource import userController, fileController, dataController
from service import tokenService
from flask_cors import CORS

app = create_app()
cors=CORS()
cors.init_app(app, supports_credentials=True)
api = Api(app, errors=errors)
api.add_resource(userController.UserRegistration, '/registration')
api.add_resource(userController.UserLogin, '/login')
api.add_resource(userController.TokenRefresh, '/updateToken')
api.add_resource(userController.Test, '/test')
api.add_resource(userController.UserLogoutAccess, '/logoutAccess')
api.add_resource(userController.UserLogoutRefresh, '/loginRefresh')
api.add_resource(userController.ChangePassword, '/changePassword')
api.add_resource(userController.ChangeUserInfo, '/changeUserinfo')
api.add_resource(fileController.UploadFile, '/uploadFile')
api.add_resource(userController.GetUserInfo, '/getUserInfo')
api.add_resource(userController.GetUserRoutes,'/getUserRoutes')
api.add_resource(fileController.JoinFile,"/autoFuzzyJoin")
api.add_resource(fileController.DownloadFile,"/file/download")
api.add_resource(dataController.GetDataName,"/getDataName")
api.add_resource(dataController.GetDataTable,'/getDataTable')
jwt = JWTManager(app)
db.init_app(app)
migrate = Migrate(app, db)
app.app_context().push()


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, decrypted_token):
    jti = decrypted_token['jti']
    return tokenService.is_jti_blacklisted(jti)


if __name__ == "__main__":
    app.run(debug=True)
