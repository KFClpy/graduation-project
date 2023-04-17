from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse

from base.baseview import BaseView
from base.status_code import Codes
from service.dataService import get_data_name
from service.fileService import get_data_from_db, get_data_from_db_with_tid
from utils.logger import base_log
data_name_parser = reqparse.RequestParser()
data_name_parser.add_argument('data_name', help='数据集名称不能为空', required=True)

class GetDataName(Resource,BaseView):
    @jwt_required()
    def post(self):
        username=get_jwt_identity()
        try:
            data={
                "data_name":get_data_name(username)
            }
            return self.formattingData(code=Codes.SUCCESS.code,msg=Codes.SUCCESS.desc,data=data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code,msg=Codes.FAILE.desc,data=None)


class GetDataTable(Resource,BaseView):
    @jwt_required()
    def post(self):
        username=get_jwt_identity()
        dataname=data_name_parser.parse_args()['data_name']
        try:
            result=get_data_from_db_with_tid(username,dataname)
            return self.formattingData(code=Codes.SUCCESS.code,msg=Codes.SUCCESS.desc,data=result)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code,msg=Codes.FAILE.desc,data=None)

