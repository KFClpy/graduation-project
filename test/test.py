import os
from time import time

import pandas as pd
from flask_jwt_extended import decode_token
from werkzeug.security import check_password_hash, generate_password_hash

from mysqldb.exts import db
from mysqldb.models import DataTableModel, DataMappingModel
from run import app
from app_config import Config
from service.fileService import get_data_from_db
from service.userService import getuser, updatepassword
# with app.app_context():
#     data=get_data_from_db("lty123456","good")
#     df=pd.DataFrame(data)
#     print(df)
#     out_path="../FIles/csv/test.csv"
#     file=df.to_csv(out_path,sep=',',index=False,header=True)