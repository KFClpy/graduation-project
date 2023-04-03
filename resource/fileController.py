import os

from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import pandas as pd

from auto_fuzzy_join.autofj import AutoFJ
from auto_fuzzy_join.datasets import load_data
from base.baseview import BaseView
from app_config import Path
from utils.filefilter import is_csv

file_parser = reqparse.RequestParser()
file_parser.add_argument('filel', type=FileStorage, location='files')
file_parser.add_argument('filer', type=FileStorage, location='files')


class Upload(Resource, BaseView):
    def post(self):
        path = Path.CSV_PATH
        data = file_parser.parse_args()
        filel = data['filel']
        filer = data['filer']
        if filel and filer and is_csv(filel.filename) and is_csv(filer.filename):
            file_path_left = os.path.join(path, secure_filename(filel.filename))
            file_path_right = os.path.join(path, secure_filename(filer.filename))
            filel.save(file_path_left)
            filer.save(file_path_right)
            left, right = load_data(file_path_left, file_path_right)
            autofj = AutoFJ(verbose=True)
            LR_joins = autofj.join(left, right, id_column="id")
            print(LR_joins)
            return LR_joins.to_dict(), 201
        return False
