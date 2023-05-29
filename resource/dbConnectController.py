from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse
from func_timeout import FunctionTimedOut
from pandas import DataFrame

from base.baseview import BaseView
from base.status_code import Codes
from service.dbConnectService import db_is_valid, db_to_dict
from service.fileService import df_to_db
from utils.logger import base_log

check_valid_parser = reqparse.RequestParser()
check_valid_parser.add_argument('username', help='数据库用户名不准为空', required=True)
check_valid_parser.add_argument('password', help='数据库密码不准为空', required=True)
check_valid_parser.add_argument('hostname', help='数据库主机名不准为空', required=True)
check_valid_parser.add_argument('port', help='数据库端口不准为空', required=True)
check_valid_parser.add_argument('database', help='数据库名不准为空', required=True)
check_valid_parser.add_argument('db_type', help='数据库类型不许为空', required=True)
execute_parser = reqparse.RequestParser()
execute_parser.add_argument('username', help='数据库用户名不准为空', required=True)
execute_parser.add_argument('password', help='数据库密码不准为空', required=True)
execute_parser.add_argument('hostname', help='数据库主机名不准为空', required=True)
execute_parser.add_argument('port', help='数据库端口不准为空', required=True)
execute_parser.add_argument('database', help='数据库名不准为空', required=True)
execute_parser.add_argument('db_type', help='数据库类型不许为空', required=True)
execute_parser.add_argument('sql', help='数据库查询语句', required=True)
execute_parser.add_argument('data_name', help='数据集名不准为空', required=True)


class CheckValid(Resource, BaseView):
    @jwt_required()
    def post(self):
        username = check_valid_parser.parse_args()['username']
        password = check_valid_parser.parse_args()['password']
        hostname = check_valid_parser.parse_args()['hostname']
        port = check_valid_parser.parse_args()['port']
        database = check_valid_parser.parse_args()['database']
        db_type = check_valid_parser.parse_args()['db_type']
        try:
            data = {
                "is_valid": db_is_valid(username, password, hostname, port, database, db_type)
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=data)
        except FunctionTimedOut:
            data = {
                "is_valid": False
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.FAILE.desc, data=data)
        except Exception as e:
            base_log.info(e)
            data = {
                "is_valid": False
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.FAILE.desc, data=data)


class ExecuteSQL(Resource, BaseView):
    @jwt_required()
    def post(self):
        my_name = get_jwt_identity()
        username = execute_parser.parse_args()['username']
        password = execute_parser.parse_args()['password']
        hostname = execute_parser.parse_args()['hostname']
        port = execute_parser.parse_args()['port']
        database = execute_parser.parse_args()['database']
        db_type = execute_parser.parse_args()['db_type']
        sql = execute_parser.parse_args()['sql']
        data_name = execute_parser.parse_args()['data_name']
        try:
            df = DataFrame(db_to_dict(username, password, hostname, port, database, db_type, sql))
            df_to_db(df, my_name, data_name)
            data = {
                "username": my_name
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.SUCCESS.desc, data=None)
        except FunctionTimedOut:
            data = {
            }
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)
        except Exception as e:
            base_log.info(e)
            data = {
            }
            return self.formattingData(code=Codes.FAILE.code, msg=Codes.FAILE.desc, data=None)
