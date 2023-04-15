from sqlalchemy import distinct

from mysqldb.exts import db
from mysqldb.models import DataTableModel


def get_data_name(username):
    data_name_list = db.session.query(distinct(DataTableModel.dataname)).filter(
        DataTableModel.username == username).all()
    if len(data_name_list) != 0:
        data_name_list = data_name_list[0]
    return list(data_name_list)
