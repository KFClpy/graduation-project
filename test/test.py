import pandas as pd
from pandas import DataFrame

import manual_fuzzy_join
from app_config import Path
from manual_fuzzy_join.join_funcion.distance_function import DistanceFunction
from manual_fuzzy_join.join_funcion.preprocessor import Preprocessor
from manual_fuzzy_join.join_funcion.tokenizer import Tokenizer
from manual_fuzzy_join.manual_join import manualJoin
from run import app

with app.app_context():
    # preprocessor = Preprocessor("lowerRemovePunctuationStem")
    # tokenizer = Tokenizer("threeGram")
    # distanceFunction = DistanceFunction("jaccardDistance")
    # df = pd.read_csv(Path.CSV_PATH + "/data_generate.csv")
    # column_pre_left = preprocessor.preprocess(df['title_l'])
    # column_pre_right = preprocessor.preprocess(df['title_r'])
    # column_token_left = tokenizer.tokenize(column_pre_left)
    # column_token_right = tokenizer.tokenize(column_pre_right)
    # df=DataFrame()
    # df['value_r']=column_token_right
    # df['value_l']=column_token_left
    # distance = distanceFunction.compute_distance(df)
    # print(distance)
    data = {
        "preprocessor": " ",
        "tokenizer": " ",
        "distance_function": []
    }
    manualJoin(DataFrame(),DataFrame(),config=data)
