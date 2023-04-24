from pandas import DataFrame

from manual_fuzzy_join import manual_join
from manual_fuzzy_join.manual_join import manualJoin
from service.fileService import get_data_from_db


def manual_join_df(user_name, data_name_left, data_name_right, data_name_generate, config):
    df_left = DataFrame(get_data_from_db(user_name, data_name_left))
    df_right = DataFrame(get_data_from_db(user_name, data_name_right))
    return manualJoin(df_left, df_right, config)
