from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from func_timeout import FunctionTimedOut

from base.baseview import BaseView
from base.status_code import Codes
from service.dbConnectService import db_is_valid
from utils.logger import base_log

check_valid_parser = reqparse.RequestParser()
check_valid_parser.add_argument('username', help='数据库用户名不准为空', required=True)
check_valid_parser.add_argument('password', help='数据库密码不准为空', required=True)
check_valid_parser.add_argument('hostname', help='数据库主机名不准为空', required=True)
check_valid_parser.add_argument('port', help='数据库端口不准为空', required=True)
check_valid_parser.add_argument('database', help='数据库名不准为空', required=True)
check_valid_parser.add_argument('db_type', help='数据库类型不许为空', required=True)


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
            data={
                "is_valid":False
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.FAILE.desc, data=data)
        except Exception as e:
            base_log.info(e)
            data = {
                "is_valid": False
            }
            return self.formattingData(code=Codes.SUCCESS.code, msg=Codes.FAILE.desc, data=data)
