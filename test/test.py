import os

from werkzeug.security import check_password_hash, generate_password_hash

from run import app
from app_config import Config
from service.userService import getuser, updatepassword
