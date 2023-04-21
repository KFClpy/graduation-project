import pandas as pd
from pandas import DataFrame

import manual_fuzzy_join
from app_config import Path
from manual_fuzzy_join.join_funcion.distance_function import DistanceFunction
from manual_fuzzy_join.join_funcion.preprocessor import Preprocessor
from manual_fuzzy_join.join_funcion.tokenizer import Tokenizer
from manual_fuzzy_join.manual_join import manualJoin
from run import app
from service.dataSetService import get_dataSet_info

with app.app_context():
    # df_left=pd.read_csv("F:/AutomaticFuzzyJoin-master/src/autofj/benchmark/TennisTournament/left.csv")
    # df_right=pd.read_csv("F:/AutomaticFuzzyJoin-master/src/autofj/benchmark/TennisTournament/right.csv")
    # data = {
    #     "preprocessor": "lowerRemovePunctuationStem",
    #     "tokenizer": "threeGram",
    #     "distance_function": {
    #         "jaccardDistance":0.5,
    #         "editDistance":0.5
    #     }
    # }
    # for key,value in manualJoin(df_left,df_right,config=data).items():
    #     if value:
    #         print(key,value)
    print(get_dataSet_info("admin123"))

