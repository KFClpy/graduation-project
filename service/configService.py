from mysqldb.exts import db
from mysqldb.models import PreprocessorModel, TokenizerModel, DistanceFunctionModel


def get_preprocessor():
    preprocessors = db.session.query(PreprocessorModel.preprocessor).all()
    result = []
    for preprocessor in preprocessors:
        result.append(preprocessor[0])
    return result


def get_tokenizer():
    tokenizers = db.session.query(TokenizerModel.tokenizer).all()
    result = []
    for tokenizer in tokenizers:
        result.append(tokenizer[0])
    return result


def get_distance_function():
    distance_functions = db.session.query(DistanceFunctionModel.distance_function).all()
    result = []
    for distance_function in distance_functions:
        result.append(distance_function[0])
    return result
