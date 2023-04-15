import os
from time import time

import pandas as pd
from flask_jwt_extended import decode_token
from werkzeug.security import check_password_hash, generate_password_hash

from auto_fuzzy_join.autofj import AutoFJ
from auto_fuzzy_join.datasets import load_data
from mysqldb.exts import db
from mysqldb.models import DataTableModel, DataMappingModel
from run import app
from app_config import Config
from service.dataService import get_data_name
from service.fileService import get_data_from_db
from service.userService import getuser, updatepassword

with app.app_context():
    print(get_data_name("admin"))