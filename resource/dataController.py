from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from base.baseview import BaseView
from base.status_code import Codes
from service.dataService import get_data_name
from utils.logger import base_log


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


