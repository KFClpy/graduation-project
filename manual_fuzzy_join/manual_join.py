from pandas import DataFrame

from manual_fuzzy_join.join_funcion.distance_function import DistanceFunction
from manual_fuzzy_join.join_funcion.preprocessor import Preprocessor
from manual_fuzzy_join.join_funcion.tokenizer import Tokenizer


def manualJoin(data_left, data_right, config):
    tokenizer = Tokenizer(config['tokenizer'])
    preprocessor = Preprocessor(config['preprocessor'])
    left_title = data_left['title']
    right_title = data_right['title']
    left_preprocess = preprocessor.preprocess(left_title)
    right_preprocess = preprocessor.preprocess(right_title)
    left_tokenizer = tokenizer.tokenize(left_preprocess)
    right_tokenizer = tokenizer.tokenize(right_preprocess)
    left_id = data_left['id']
    right_id = data_right['id']
    left_result = {}
    for index,value in left_id.items():
        left_result[value] = []
    distance_functions = config['distance_function']
    for key, value in distance_functions.items():
        threshold = value
        distance_function = key
        for i, v in left_tokenizer.items():
            result_id = child_join(v, right_tokenizer, threshold, distance_function, right_id)
            index_id = left_id[i]
            if result_id is None:
                continue
            left_result[index_id].append(result_id)
    return left_result


def child_join(left_title, series_right, threshold, distance_function, right_id):
    distanceFunction = DistanceFunction(distance_function)
    df = DataFrame()
    df['value_r'] = series_right
    df['value_l'] = [left_title] * len(df.index)
    distance_series = distanceFunction.compute_distance(df)
    minId = right_id[distance_series.idxmin()]
    if distance_series.min() > threshold:
        minId = None
    return minId
