from sqlalchemy import distinct, func

from exception.ColumnOutOfMaxException import ColumnOutOfMax
from mysqldb.exts import db
from mysqldb.models import DataMappingModel, DataTableModel


def get_dataset_info(username):
    dataname_count = db.session.query(DataTableModel.dataname, func.count(DataTableModel.tid)). \
        filter(DataTableModel.username == username).group_by(DataTableModel.dataname).all()
    dataname_mappings = db.session.query(DataMappingModel.dataname, func.count(DataMappingModel.th_name)).filter(
        DataMappingModel.username == username).group_by(DataMappingModel.dataname).all()
    data_name = {}
    for value in dataname_mappings:
        data_name[value[0]] = {"rows":0,'columns':0}
        data_name[value[0]]['columns']=value[1]
    for value in dataname_count:
        data_name[value[0]]['rows']=(value[1])
    result = []
    for key, value in data_name.items():
        data_now = {'data_name': key, 'columns': value['columns'], 'rows': value['rows']}
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


def delete_column(username, dataname, columnid):
    try:
        count = db.session.query(func.count(DataMappingModel.th_id)). \
            filter(DataMappingModel.username == username, DataMappingModel.dataname == dataname).first()[0]
        if count > 1:
            db.session.query(DataMappingModel).filter(DataMappingModel.username == username,
                                                      DataMappingModel.dataname == dataname,
                                                      DataMappingModel.th_id == columnid).delete()
        else:
            if db.session.query(DataMappingModel.th_id).filter(DataMappingModel.dataname == dataname,
                                                               DataMappingModel.username == username). \
                    first()[0] == int(columnid):
                db.session.query(DataTableModel).filter(DataTableModel.dataname == dataname,
                                                        DataTableModel.username == username).delete()
                db.session.query(DataMappingModel).filter(DataMappingModel.dataname == dataname,
                                                          DataMappingModel.username == username).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def get_column_info(username, dataname):
    datas = db.session.query(DataMappingModel).filter(
        DataMappingModel.username == username, DataMappingModel.dataname == dataname).all()
    result = []
    for data in datas:
        now = {"column_id": data.th_id, "column_name": data.th_name}
        result.append(now)
    return result


def edit_column(username, dataname, columnid, newcolumnname):
    try:
        data = db.session.query(DataMappingModel).filter(DataMappingModel.username == username,
                                                         DataMappingModel.dataname == dataname,
                                                         DataMappingModel.th_id == columnid).first()
        data.th_name = newcolumnname
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def add_column(user_name, data_name, column_name, default_value):
    try:
        top_id = db.session.query(func.max(DataMappingModel.th_id)).filter(DataMappingModel.username == user_name,
                                                                           DataMappingModel.dataname == data_name).first()[
            0]
        now_id = top_id + 1
        if now_id > 14:
            raise ColumnOutOfMax("列数超出限制")
        new_map = DataMappingModel()
        new_map.dataname = data_name
        new_map.username = user_name
        new_map.th_id = now_id
        new_map.th_name = column_name
        db.session.add(new_map)
        attributes = ['attribute%s' % i for i in range(1, 16)]
        now_column = attributes[now_id]
        rows = db.session.query(DataTableModel).filter(DataTableModel.dataname == data_name,
                                                       DataTableModel.username == user_name).all()
        for row in rows:
            setattr(row, now_column, default_value)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
