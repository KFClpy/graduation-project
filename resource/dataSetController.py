from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse

from base.baseview import BaseView
from base.status_code import Codes
from service.dataSetService import get_dataset_info, delete_dataset_info
from utils.logger import base_log

dataSetParser = reqparse.RequestParser()
dataSetParser.add_argument("data_name", required=True, help="数据集名称不允许为空")


class GetDataInfo(Resource, BaseView):
    @jwt_required()
    def post(self):
        user_name = get_jwt_identity()
        try:
            back_data = get_dataset_info(user_name)
            return self.formattingData(Codes.SUCCESS.code, Codes.SUCCESS.desc, data=back_data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(Codes.FAILE.code, Codes.FAILE.desc, data=None)


class DeleteDataInfo(Resource, BaseView):
    @jwt_required()
    def post(self):
        user_name = get_jwt_identity()
        data_name = dataSetParser.parse_args()['data_name']
        try:
            delete_dataset_info(user_name, data_name)
            back_data = {
                "username": user_name
            }
            return self.formattingData(Codes.SUCCESS.code, Codes.SUCCESS.desc, data=back_data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(Codes.FAILE.code, Codes.FAILE.desc, data=None)