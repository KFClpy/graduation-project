import json

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse

from base.baseview import BaseView
from base.status_code import Codes
from service.dataService import get_data_name, delete_one_data, edit_one_data, add_one_data, searchSomeData
from service.fileService import get_data_from_db, get_data_from_db_with_tid
from utils.logger import base_log

data_name_parser = reqparse.RequestParser()
data_name_parser.add_argument('data_name', help='数据集名称不能为空', required=True)
data_tid_parser = reqparse.RequestParser()
data_tid_parser.add_argument('tid', help='数据tid不能为空', required=True)
data_edit_parser = reqparse.RequestParser()
data_edit_parser.add_argument('tid', help='数据tid不能为空', required=True)
data_edit_parser.add_argument('data', help='数据本体不能为空', required=True)
data_add_parser = reqparse.RequestParser()
data_add_parser.add_argument('data', help='数据本体不能为空', required=True)
data_add_parser.add_argument('data_name', help='数据集名称不能为空', required=True)
data_search_parser=reqparse.RequestParser()
data_search_parser.add_argument('data_type',help='数据类型不能为空',required=True)
data_search_parser.add_argument('data_value',help='数据值不能为空',required=True)
data_search_parser.add_argument('data_name',help='数据集名称不能为空',required=True)

class GetDataName(Resource, BaseView):
    @jwt_required()
    def post(self):
        username = get_jwt_identity()
        try:
            data = {
                "data_name": get_data_name(username)
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)


class GetDataTable(Resource, BaseView):
    @jwt_required()
    def post(self):
        username = get_jwt_identity()
        dataname = data_name_parser.parse_args()['data_name']
        try:
            result = get_data_from_db_with_tid(username, dataname)
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=result)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)


class DeleteOneData(Resource, BaseView):
    @jwt_required()
    def post(self):
        tid = data_tid_parser.parse_args()['tid']
        user_name = get_jwt_identity()
        try:
            delete_one_data(tid)
            back_data = {
                "username": user_name
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=back_data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)


class EditOneData(Resource, BaseView):
    @jwt_required()
    def post(self):
        tid = data_edit_parser.parse_args()['tid']
        user_name = get_jwt_identity()
        try:
            data = eval(data_edit_parser.parse_args()['data'])
            edit_one_data(tid, data)
            back_data = {
                "username": user_name
            }
            return self.formattingData(Codes.SUCCESS.code, Codes.SUCCESS.desc, data=back_data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(Codes.FAILE.code, Codes.FAILE.desc, data=None)


class AddOneData(Resource, BaseView):
    @jwt_required()
    def post(self):
        user_name = get_jwt_identity()
        try:
            data = eval(data_add_parser.parse_args()['data'])
            data_name = data_add_parser.parse_args()['data_name']
            add_one_data(data, data_name, user_name)
            back_data = {
                "username": user_name
            }
            return self.formattingData(Codes.SUCCESS.code, Codes.SUCCESS.desc, data=back_data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(Codes.FAILE.code, Codes.FAILE.desc, data=None)


class SearchSomeData(Resource,BaseView):
    @jwt_required()
    def post(self):
        user_name=get_jwt_identity()
        try:
            data_type=data_search_parser.parse_args()['data_type']
            data_value=data_search_parser.parse_args()['data_value']
            data_name=data_search_parser.parse_args()['data_name']
            data=searchSomeData(data_name=data_name,data_value=data_value,data_type=data_type,user_name=user_name)
            back_data={
                "data":data
            }
            return self.formattingData(Codes.SUCCESS.code, Codes.SUCCESS.desc, data=back_data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(Codes.FAILE.code,Codes.FAILE.desc,data=None)
