import os
from time import time

from flask_jwt_extended import decode_token
from werkzeug.security import check_password_hash, generate_password_hash

from run import app
from app_config import Config
from service.userService import getuser, updatepassword


