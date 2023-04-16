import pandas as pd
from pandas import DataFrame

from exception.ColumnOutOfMaxException import ColumnOutOfMax
from exception.DataSetAlreadyExistException import DataSetAlreadyExist
from mysqldb.exts import db
from mysqldb.models import DataTableModel, DataMappingModel
from service.dataService import has_data_name


def file_to_data(filepath, username, dataname):
    df = pd.read_csv(filepath)
    attributes = ['attribute%s' % i for i in range(1, 16)]
    try:
        th_list = df.columns.tolist()
        if len(th_list)>15:
            raise ColumnOutOfMax("列数超出限制")
        if has_data_name(username,dataname):
            raise  DataSetAlreadyExist("数据集已存在")
        for index, value in enumerate(th_list):
            mapping = DataMappingModel()
            mapping.username = username
            mapping.dataname = dataname
            setattr(mapping, 'th_id', index)
            setattr(mapping, 'th_name', value)
            db.session.add(mapping)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    try:
        for index, row in df.iterrows():
            data = DataTableModel()
            for i in range(row.size):
                setattr(data, attributes[i], row[i])
            data.username = username
            data.dataname = dataname
            db.session.add(data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def df_to_db(df,username, dataname):
    attributes = ['attribute%s' % i for i in range(1, 16)]
    try:
        th_list = df.columns.tolist()
        if len(th_list)>15:
            raise ColumnOutOfMax("列数超出限制")
        if has_data_name(username,dataname):
            raise  DataSetAlreadyExist("数据集已存在")
        for index, value in enumerate(th_list):
            mapping = DataMappingModel()
            mapping.username = username
            mapping.dataname = dataname
            setattr(mapping, 'th_id', index)
            setattr(mapping, 'th_name', value)
            db.session.add(mapping)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    try:
        for index, row in df.iterrows():
            data = DataTableModel()
            for i in range(row.size):
                setattr(data, attributes[i], row[i])
            data.username = username
            data.dataname = dataname
            db.session.add(data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def get_data_from_db(username, dataname):
    try:
        rows = db.session.query(DataTableModel).filter(DataTableModel.username == username,
                                                       DataTableModel.dataname == dataname).\
            order_by(DataTableModel.attribute1).all()
    except Exception as e:
        raise e
    try:
        mappings = db.session.query(DataMappingModel).filter(DataMappingModel.username == username,
                                                             DataMappingModel.dataname == dataname).all()
    except Exception as e:
        raise e
    db_dict = {}
    attributes = ['attribute%s' % i for i in range(1, 16)]
    for mapping in mappings:
        db_dict[mapping.th_name] = []
    for row in rows:
        for mapping in mappings:
            db_dict[mapping.th_name].append(getattr(row, attributes[mapping.th_id]))
    return db_dict

