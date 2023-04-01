import os

from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from base.baseview import BaseView
from app_config import  Path

file_parser = reqparse.RequestParser()
file_parser.add_argument('file', type=FileStorage, location='files')


class Upload(Resource, BaseView):
    def post(self):
        path = Path.CSV_PATH
        data = file_parser.parse_args()
        file = data['file']
        file_path = os.path.join(path, secure_filename(file.filename))
        file.save(file_path)
        return file.filename, 201
