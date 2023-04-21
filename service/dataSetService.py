from sqlalchemy import distinct, func

from mysqldb.exts import db
from mysqldb.models import DataMappingModel, DataTableModel


def get_dataset_info(username):
    dataname_mappings = db.session.query(DataMappingModel.dataname, func.count(DataMappingModel.th_name)).filter(
        DataMappingModel.username == username).group_by(DataMappingModel.dataname).all()
    dataname_count = db.session.query(DataTableModel.dataname, func.count(DataTableModel.tid)). \
        filter(DataTableModel.username == username).group_by(DataTableModel.dataname).all()
    data_name = {}
    for value in dataname_mappings:
        data_name[value[0]] = []
        data_name[value[0]].append(value[1])
    for value in dataname_count:
        data_name[value[0]].append(value[1])
    return data_name
