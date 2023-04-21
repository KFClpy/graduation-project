from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from base.baseview import BaseView
from base.status_code import Codes
from service.dataSetService import get_dataset_info
from utils.logger import base_log


class GetDataInfo(Resource,BaseView):
    @jwt_required()
    def post(self):
        user_name=get_jwt_identity()
        try:
            back_data= get_dataset_info(user_name)
            return self.formattingData(Codes.SUCCESS.code,Codes.SUCCESS.desc,data=back_data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(Codes.FAILE.code,Codes.FAILE.desc,data=None)


