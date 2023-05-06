from sqlalchemy import distinct

from mysqldb.exts import db
from mysqldb.models import DataTableModel, DataMappingModel


def get_data_name(username):
    data_name_list = db.session.query(distinct(DataTableModel.dataname)).filter(
        DataTableModel.username == username).all()
    result_list = []
    if len(data_name_list) != 0:
        for data_name in data_name_list:
            result_list.append(data_name[0])
    return result_list


def has_data_name(username, dataname):
    data_name_list = db.session.query(DataTableModel).filter(DataTableModel.username == username,
                                                             DataTableModel.dataname == dataname).all()
    if len(data_name_list) > 0:
        return True
    return False


def find_username_dataname(tid):
    data_row = db.session.query(DataTableModel).filter(DataTableModel.tid == tid).first()
    return data_row.username, data_row.dataname


def delete_one_data(tid):
    try:
        db.session.query(DataTableModel).filter(DataTableModel.tid == tid).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def edit_one_data(tid, data):
    try:
        username, dataname = find_username_dataname(tid)
        mappings = db.session.query(DataMappingModel).filter(DataMappingModel.username == username,
                                                             DataMappingModel.dataname == dataname).all()
    except Exception as e:
        raise e
    try:
        data_row = db.session.query(DataTableModel).filter(DataTableModel.tid == tid).first()
        attributes = ['attribute%s' % i for i in range(1, 16)]
        for mapping in mappings:
            if type(getattr(data_row, attributes[mapping.th_id])) == type(data[mapping.th_name]):
                setattr(data_row, attributes[mapping.th_id], data[mapping.th_name])
            else:
                setattr(data_row, attributes[mapping.th_id], int(data[mapping.th_name]))
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def add_one_data(data, data_name, user_name):
    data_row = DataTableModel()
    data_row.username = user_name
    data_row.dataname = data_name
    try:
        mappings = db.session.query(DataMappingModel).filter(DataMappingModel.username == user_name,
                                                             DataMappingModel.dataname == data_name).all()
    except Exception as e:
        raise e
    try:
        attributes = ['attribute%s' % i for i in range(1, 16)]
        for mapping in mappings:
            if type(getattr(data_row, attributes[mapping.th_id])) == type(data[mapping.th_name]):
                setattr(data_row, attributes[mapping.th_id], data[mapping.th_name])
            else:
                setattr(data_row, attributes[mapping.th_id], int(data[mapping.th_name]))
        db.session.add(data_row)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def searchSomeData(user_name, data_type, data_name, data_value):
    try:
        mappings = db.session.query(DataMappingModel).filter(DataMappingModel.username == user_name,
                                                             DataMappingModel.dataname == data_name).all()
        attributes = ['attribute%s' % i for i in range(1, 16)]
        dict_map = {}
        for mapping in mappings:
            dict_map[mapping.th_name] = mapping.th_id
        search_type = attributes[dict_map[data_type]]
        data_rows = db.session.query(DataTableModel).filter(DataTableModel.username == user_name,
                                                            DataTableModel.dataname == data_name,
                                                            getattr(DataTableModel, search_type) == data_value)
    except Exception as e:
        raise e
    db_dict = {}
    attributes = ['attribute%s' % i for i in range(1, 16)]
    for mapping in mappings:
        db_dict[mapping.th_name] = []
    db_dict['tid'] = []
    for row in data_rows:
        for mapping in mappings:
            db_dict[mapping.th_name].append(getattr(row, attributes[mapping.th_id]))
        db_dict['tid'].append(row.tid)
    return db_dict
