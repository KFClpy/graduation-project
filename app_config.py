import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'fuzzy_join'
    USERNAME = 'root'
    PASSWORD = '123456'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT,
                                                                                   DATABASE)
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = '0'
    REDIS_PWD = 'lty542217'
    JWT_SECRET_KEY = 'jwt-secret-string'
    JWT_BLOCKLIST_TOKEN_CHECKS = ['access', 'refresh']
