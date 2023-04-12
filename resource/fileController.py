import os

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import pandas as pd

from auto_fuzzy_join.autofj import AutoFJ
from auto_fuzzy_join.datasets import load_data
from base.baseview import BaseView
from app_config import Path
from base.status_code import Codes
from service.fileService import file_to_data
from utils.filefilter import is_csv


data_file_parser = reqparse.RequestParser()
data_file_parser.add_argument('data_name', help='数据集名称不能为空', required=True,location='form')
data_file_parser.add_argument('data_file', type=FileStorage, location='files')


class UploadFile(Resource, BaseView):
    @jwt_required()
    def post(self):
        user_name = get_jwt_identity()
        path = Path.CSV_PATH
        data = data_file_parser.parse_args()
        data_name = data['data_name']
        data_file = data['data_file']
        if data_file and is_csv(data_file.filename):
            file_path = os.path.join(path, secure_filename(data_file.filename))
            data_file.save(file_path)
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc,
                                       data=file_to_data(file_path, user_name, data_name))
        return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)
