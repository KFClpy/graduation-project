from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_jwt
from flask_restful import Resource, reqparse

from base.baseview import BaseView
from base.status_code import Codes
from mysqldb.models import User
from service.userService import login_user, register_user, logout, getuser, updatepassword, updateuser
from utils.logger import base_log

parser = reqparse.RequestParser()
parser.add_argument('username', help='用户名不能为空', required=True)
parser.add_argument('password', help='密码不能为空', required=True)
userParser = reqparse.RequestParser()
userParser.add_argument('gender', help='性别不能为空', required=True)
userParser.add_argument('phone', help='电话不能为空', required=True)
userParser.add_argument('email', help='邮件地址不能为空', required=True)
userParser.add_argument('nickname', help='昵称不能为空', required=True)
userParser.add_argument('avatar')
passwordParser = reqparse.RequestParser()
passwordParser.add_argument('oldpassword', help='旧密码不能为空', required=True)
passwordParser.add_argument('newpassword', help='新密码不能为空', required=True)


class UserRegistration(Resource, BaseView):
    def post(self):
        data = parser.parse_args()
        new_user = User(
            tusername=data['username'],
            role='user'
        )
        new_user.set_password(data['password'])
        try:
            register_user(new_user)
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=None)

        except Exception as ex:
            base_log.info(ex)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)


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
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        data = {'access_token': access_token}
        return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.FAILE.desc, data=data)


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
        userinfo = userParser.parse_args()
        current_user = get_jwt_identity()
        newuser = User(tusername=current_user, avatar=userinfo['avatar'], email=userinfo['email'],
                       phone=userinfo['phone'], gender=userinfo['gender'], nickname=userinfo['nickname'])
        try:
            updateuser(newuser)
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=None)
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
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=None)


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


class Test(Resource):
    @jwt_required()
    def post(self):
        return {
            "message": "5000"
        }
