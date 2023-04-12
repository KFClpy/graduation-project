import pandas as pd


def file_to_data(filepath, username, dataname):
    df = pd.read_csv(filepath)
    df['username'] = username
    df['dataname'] = dataname
    return df.to_dict()