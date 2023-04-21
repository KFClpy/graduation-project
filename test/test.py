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
    df_left=pd.read_csv("F:/AutomaticFuzzyJoin-master/src/autofj/benchmark/TennisTournament/left.csv")
    df_right=pd.read_csv("F:/AutomaticFuzzyJoin-master/src/autofj/benchmark/TennisTournament/right.csv")
    data = {
        "preprocessor": "lowerRemovePunctuationStem",
        "tokenizer": "threeGram",
        "distance_function": {
            "jaccardDistance":0.5
        }
    }
    print(manualJoin(df_left,df_right,config=data))
