from func_timeout import func_set_timeout
from sqlalchemy import create_engine, event, text


@func_set_timeout(10)
def db_is_valid(username, password, hostname, port, database, db_type):
    if db_type == 'mysql':
        uri = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(username, password, hostname, port,
                                                                   database)
    elif db_type == 'postgresql':
        uri = 'postgresql://{}:{}@{}:{}/{}'.format(username, password, hostname, port,
                                                   database)
    else:
        uri = ""
    engine = create_engine(uri)
    conn = engine.connect()
    result = conn.execute(text('select 1+3'))
    return result is not None


@func_set_timeout(30)
def db_to_dict(username, password, hostname, port, database, db_type, sql):
    sql_word=sql.split()
    table_name = sql_word[sql_word.index('from')+1]

    if db_type == 'mysql':
        uri = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(username, password, hostname, port,
                                                                   database)
        sql_column="select column_name from information_schema.columns where table_schema='{}' and table_name='{}'".format(database,table_name)
    elif db_type == 'postgresql':
        uri = 'postgresql://{}:{}@{}:{}/{}'.format(username, password, hostname, port,
                                                   database)
        sql_column = sql_column = "select column_name from information_schema.columns where table_schema='public' and table_name='{}'".format(table_name)
    else:
        uri = ""
    engine = create_engine(uri)
    conn = engine.connect()
    result = conn.execute(text(sql))
    column_name = conn.execute(text(sql_column))
    column = column_name.fetchall()
    column_list = []
    for col in column:
        column_list.append(col[0])
    res = result.fetchall()
    df_dict = {}
    for col in column_list:
        df_dict[col] = []
    for r in res:
        index = 0
        for val in r:
            df_dict[column_list[index]].append(val)
            index += 1

    return df_dict
