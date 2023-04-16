from sqlalchemy import distinct

from mysqldb.exts import db
from mysqldb.models import DataTableModel


def get_data_name(username):
    data_name_list = db.session.query(distinct(DataTableModel.dataname)).filter(
        DataTableModel.username == username).all()
    result_list=[]
    if len(data_name_list) != 0:
        for data_name in data_name_list:
            result_list.append(data_name[0])
    return result_list
