from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse

from base.baseview import BaseView
from base.status_code import Codes
from service.userListService import get_user_list, delete_user, edit_user
from utils.logger import base_log

delete_parser = reqparse.RequestParser()
delete_parser.add_argument("user_name", help="删除的用户名不准为空", required=True)
edit_parser = reqparse.RequestParser()
edit_parser.add_argument("user_name", help="编辑的用户名不准为空", required=True)
edit_parser.add_argument("model", help="实体类不许为空", required=True)
deletes_parser = reqparse.RequestParser()
deletes_parser.add_argument("user_names", help="删除的用户名不准为空", required=True, action='split')


class GetUserList(Resource, BaseView):
    @jwt_required()
    def post(self):
        user_name = get_jwt_identity()
        try:
            data = {
                "userList": get_user_list(user_name)
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)


class DeleteUser(Resource, BaseView):
    @jwt_required()
    def post(self):
        user_name = get_jwt_identity()
        delete_user_name = delete_parser.parse_args()['user_name']
        try:
            delete_user(delete_user_name)
            data = {
                "username": user_name
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)


class EditUser(Resource, BaseView):
    @jwt_required()
    def post(self):
        user_name = get_jwt_identity()
        edit_user_name = edit_parser.parse_args()['user_name']
        entity = eval(edit_parser.parse_args()['model'])
        try:
            edit_user(edit_user_name, entity['gender'], entity['phone'], entity['email'])
            data = {
                "username": user_name
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)


class DeleteUsers(Resource, BaseView):
    @jwt_required()
    def post(self):
        user_name = get_jwt_identity()
        names = deletes_parser.parse_args()['user_names']
        try:
            if type(names) == 'list':
                for name in names:
                    delete_user(name)
            else:
                delete_user(names)
            data = {
                "username": user_name
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)
