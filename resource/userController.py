from datetime import timedelta
from time import time

from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_jwt, decode_token
from flask_restful import Resource, reqparse

from base.baseview import BaseView
from base.status_code import Codes
from mysqldb.models import User
from routes import routes
from routes.home import home_route
from service.userListService import search_user
from service.userService import login_user, register_user, logout, getuser, updatepassword, updateuser, get_self
from utils.logger import base_log

parser = reqparse.RequestParser()
parser.add_argument('username', help='用户名不能为空', required=True)
parser.add_argument('password', help='密码不能为空', required=True)
userParser = reqparse.RequestParser()
userParser.add_argument('userInfo', help='用户不能为空', required=True)
passwordParser = reqparse.RequestParser()
passwordParser.add_argument('oldpassword', help='旧密码不能为空', required=True)
passwordParser.add_argument('newpassword', help='新密码不能为空', required=True)
tokenParser = reqparse.RequestParser()
tokenParser.add_argument('refreshToken', help='token不能为空', required=True)


class UserRegistration(Resource, BaseView):
    def post(self):
        data = parser.parse_args()
        new_user = User(
            tusername=data['username'],
            role='user'
        )
        backdata = {
            'username': "notgood"
        }
        new_user.set_password(data['password'])
        try:
            register_user(new_user)
            backdata['username'] = new_user.tusername
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=backdata)

        except Exception as ex:
            base_log.info(ex)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=backdata)


class UserLogin(Resource, BaseView):
    def post(self):
        data = parser.parse_args()
        new_user = User(
            tusername=data['username'],
            tpassword=data['password']
        )

        try:
            data = login_user(new_user)
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=data)

        except Exception as ex:
            base_log.info(ex)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)


class TokenRefresh(Resource, BaseView):
    def post(self):
        refresh_token = tokenParser.parse_args()['refreshToken']
        current_user = decode_token(refresh_token, allow_expired=True)['sub']
        expire_time = decode_token(refresh_token, allow_expired=True)['exp']
        if int(time()) <= expire_time:
            access_token = create_access_token(identity=current_user, expires_delta=timedelta(minutes=30))
            data = {'token': access_token, 'refreshToken': refresh_token}
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=data)
        else:
            return self.formattingData(code=Codes.FAILE.code, msg="登录已过期", data=None)


class ChangePassword(Resource, BaseView):
    @jwt_required()
    def post(self):
        pwdinfo = passwordParser.parse_args()
        current_user = get_jwt_identity()
        try:
            updatepassword(pwdinfo['newpassword'], pwdinfo['oldpassword'], current_user)
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=None)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)


class ChangeUserInfo(Resource, BaseView):
    @jwt_required()
    def post(self):
        user_name = get_jwt_identity()
        userinfo = eval(userParser.parse_args()['userInfo'])
        current_user = get_jwt_identity()
        newuser = User(tusername=current_user, email=userinfo['email'],
                       phone=userinfo['phone'], gender=userinfo['gender'])
        try:
            updateuser(newuser)
            data = {
                "username": user_name
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)


class UserLogoutAccess(Resource, BaseView):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        try:
            logout(jti)
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=None)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)


class UserLogoutRefresh(Resource, BaseView):
    @jwt_required(refresh=True)
    def post(self):
        jti = get_jwt()['jti']
        try:
            logout(jti)
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=None)
        except Exception as e:
            base_log.log(e)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)


class GetUserInfo(Resource, BaseView):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        try:
            user = getuser(current_user)
            data = {
                'userName': user.tusername,
                'userId': user.uid,
                'userRole': user.role
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)


class GetUserRoutes(Resource, BaseView):
    @jwt_required()
    def post(self):
        username = get_jwt_identity()
        try:
            user = getuser(username)
            data = {
                "routes": routes[user.role],
                "home": home_route
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)


class GetSelfInfo(Resource, BaseView):
    @jwt_required()
    def post(self):
        username = get_jwt_identity()
        try:
            data = {
                "userInfo": get_self(username)
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)


class Test(Resource):
    @jwt_required()
    def post(self):
        return {
            "message": "5000"
        }
