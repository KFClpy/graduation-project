from werkzeug.security import check_password_hash, generate_password_hash

from run import app
from service.userService import getuser, updatepassword

