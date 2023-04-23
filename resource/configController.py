from flask_jwt_extended import jwt_required
from flask_restful import Resource

from base.baseview import BaseView
from base.status_code import Codes
from service.configService import get_preprocessor, get_tokenizer, get_distance_function
from utils.logger import base_log


class GetPreprocessor(Resource, BaseView):
    @jwt_required()
    def post(self):
        try:
            preprocessor = get_preprocessor()
            data = {
                "preprocessor": preprocessor
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)


class GetTokenizer(Resource, BaseView):
    @jwt_required()
    def post(self):
        try:
            tokenizer = get_tokenizer()
            data = {
                "tokenizer": tokenizer
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)


class GetDistanceFunction(Resource, BaseView):
    @jwt_required()
    def post(self):
        try:
            distance_function = get_distance_function()
            data = {
                "distance_function": distance_function
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=data)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)
