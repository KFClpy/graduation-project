import re

from nltk import PorterStemmer

ps = PorterStemmer()


def lower(x):
    return str(x).lower()


def removePunctuation(x):
    return re.sub(r'[^\w\s]', '', x)


def stem(x):
    return " ".join([ps.stem(w) for w in x.split()])


def lowerStem(x):
    x = lower(x)
    x = stem(x)
    return x


def lowerRemovePunctuation(x):
    x = lower(x)
    x = removePunctuation(x)
    return x


def lowerRemovePunctuationStem(x):
    x = lower(x)
    x = removePunctuation(x)
    x = stem(x)
    return x


class Preprocessor:
    def __init__(self, method):
        self.method = method
        if method == "lower":
            self.func = lower
        elif method == "lowerStem":
            self.func = lowerStem
        elif method == "lowerRemovePunctuation":
            self.func = lowerRemovePunctuation
        elif method == "lowerRemovePunctuationStem":
            self.func = lowerRemovePunctuationStem
        else:
            raise Exception("{} is an invalid preprocessing method"
                            .format(method))

    def preprocess(self, X):
        """ Preprocess the given data

        Parameters
        ----------
        X: pd.Series
            Input data
        """
        X = X.apply(self.func)
        return X
