import pandas as pd

from mysqldb.exts import db
from mysqldb.models import DataTableModel, DataMappingModel


def file_to_data(filepath, username, dataname):
    df = pd.read_csv(filepath)
    df['username'] = username
    df['dataname'] = dataname
    attributes = ['attribute%s' % i for i in range(1, 16)]
    try:
        th_list = df.columns.tolist()
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
