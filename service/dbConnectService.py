from func_timeout import func_set_timeout
from sqlalchemy import create_engine, event, text


@func_set_timeout(10)
def db_is_valid(username, password, hostname, port, database, type):
    if type == 'mysql':
        uri = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(username, password, hostname, port,
                                                                   database)
    elif type == 'postgresql':
        uri = 'postgresql://{}:{}@{}:{}/{}'.format(username, password, hostname, port,
                                                   database)
    else:
        uri = ""
    engine = create_engine(uri)
    conn = engine.connect()
    result = conn.execute(text('select 1+3'))
    return result is not None
