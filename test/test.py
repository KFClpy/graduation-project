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
from service.fileService import get_data_from_db
from service.userService import getuser, updatepassword

with app.app_context():
    autofj = AutoFJ(verbose=True)
    datal = get_data_from_db("lty123456", "left1")
    datar = get_data_from_db("lty123456", "right")
    left, right = load_data("C:\\Users\\DELL\\Desktop\\left.csv", "C:\\Users\\DELL\\Desktop\\right.csv")
    result1 = autofj.join(left, right, id_column="id")
    print(result1)
    # dfl = pd.DataFrame(datal)
    # dfr = pd.DataFrame(datar)
    # result = autofj.join(dfl, dfr, "id")
    # print(result)
    # out_path = "../FIles/csv/test.csv"
    # file = result.to_csv(out_path, sep=',', index=False, header=True)
