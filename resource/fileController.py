import os

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse
from pandas import DataFrame
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import pandas as pd

from auto_fuzzy_join.autofj import AutoFJ
from auto_fuzzy_join.datasets import load_data
from base.baseview import BaseView
from app_config import Path
from base.status_code import Codes
from service.fileService import file_to_data, get_data_from_db
from utils.filefilter import is_csv
from utils.logger import base_log

data_file_parser = reqparse.RequestParser()
data_file_parser.add_argument('data_name', help='数据集名称不能为空', required=True, location='form')
data_file_parser.add_argument('data_file', type=FileStorage, location='files')
join_parser = reqparse.RequestParser()
join_parser.add_argument('left_data_name',help='左侧数据集名称不能为空',required=True)
join_parser.add_argument('right_data_name',help='右侧数据集名称不能为空',required=True)


class UploadFile(Resource, BaseView):
    @jwt_required()
    def post(self):
        user_name = get_jwt_identity()
        path = Path.CSV_PATH
        data = data_file_parser.parse_args()
        data_name = data['data_name']
        data_file = data['data_file']
        if data_file and is_csv(data_file.filename):
            try:
                file_path = os.path.join(path, secure_filename(data_file.filename))
                data_file.save(file_path)
                file_to_data(file_path, user_name, data_name)
                os.remove(file_path)
                return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc,
                                           data=None)
            except Exception as ex:
                base_log.info(ex)
                return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)
        return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)


class JoinFile(Resource, BaseView):
    @jwt_required()
    def post(self):
        data = join_parser.parse_args()
        left_name = data['left_data_name']
        right_name = data['right_data_name']
        user_name=get_jwt_identity()
        try:
            left=get_data_from_db(username=user_name,dataname=left_name)
            right=get_data_from_db(username=user_name,dataname=right_name)
            df_left=DataFrame(left)
            df_right=DataFrame(right)
            autofj = AutoFJ(verbose=True)
            result = autofj.join(df_left, df_right, id_column="id").to_dict()
            return self.formattingData(code=Codes.SUCCESS.code,msg=Codes.SUCCESS.desc,data=result)
        except Exception as e:
            base_log.info(e)
            return self.formattingData(code=Codes.FAILE.code,msg=Codes.FAILE.desc,data=None)
