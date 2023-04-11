import os
from time import time

from flask_jwt_extended import decode_token
from werkzeug.security import check_password_hash, generate_password_hash

from run import app
from app_config import Config
from service.userService import getuser, updatepassword

with app.app_context():
    data = decode_token(
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4MTAyNDAzOSwianRpIjoiNmQ2N2I5MDctYTY2Ni00NDdjLWJiNjItYzZlYzVhYWUwYWNlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imx0eSIsIm5iZiI6MTY4MTAyNDAzOSwiZXhwIjoxNjgxMDI0OTM5fQ.xi86Ff48_SGqTvhAjHjFN3JCsh0DPqJ0UFNmYvy3HJY",
        allow_expired=True)
    print(data['exp'])
    time_now = int(time())
    print(data['exp'] >= time_now)
