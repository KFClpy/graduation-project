from sqlalchemy import distinct, func

from mysqldb.exts import db
from mysqldb.models import DataMappingModel, DataTableModel


def get_dataset_info(username):
    dataname_count = db.session.query(DataTableModel.dataname, func.count(DataTableModel.tid)). \
        filter(DataTableModel.username == username).group_by(DataTableModel.dataname).all()
    dataname_mappings = db.session.query(DataMappingModel.dataname, func.count(DataMappingModel.th_name)).filter(
        DataMappingModel.username == username).group_by(DataMappingModel.dataname).all()
    data_name = {}
    for value in dataname_mappings:
        data_name[value[0]] = []
        data_name[value[0]].append(value[1])
    for value in dataname_count:
        data_name[value[0]].append(value[1])
    result = []
    for key, value in data_name.items():
        data_now = {'data_name': key, 'columns': value[0], 'rows': value[1]}
        result.append(data_now)
    return result


def delete_dataset_info(username, dataname):
    try:
        db.session.query(DataTableModel).filter(DataTableModel.dataname == dataname,
                                                DataTableModel.username == username).delete()
        db.session.query(DataMappingModel).filter(DataMappingModel.dataname == dataname,
                                                  DataMappingModel.username == username).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
