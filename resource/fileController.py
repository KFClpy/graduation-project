import os

from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import pandas as pd
from base.baseview import BaseView
from app_config import  Path
from utils.filefilter import is_csv

file_parser = reqparse.RequestParser()
file_parser.add_argument('file', type=FileStorage, location='files')


class Upload(Resource, BaseView):
    def post(self):
        path = Path.CSV_PATH
        data = file_parser.parse_args()
        file = data['file']
        if file and is_csv(file.filename):
            file_path = os.path.join(path, secure_filename(file.filename))
            file.save(file_path)
            df=pd.read_csv(file_path)
            return df.__len__(), 201
        return False