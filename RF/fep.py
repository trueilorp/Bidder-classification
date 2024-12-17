import pandas as pd
from typing import Callable


def load_features(path:str):
    data = pd.read_csv(path)
    return data


class FEP:
    def __init__(self, path:str):
        self.path = path

    def save_features(self):
        self.data.to_csv(f'{self.path}', index=False)

    def extract_features(self, df:pd.DataFrame, feature_function: Callable[[pd.DataFrame], pd.DataFrame]):
        self.data = feature_function(df)
        return self.data

    def run(self, df:pd.DataFrame, feature_function: Callable[[pd.DataFrame], pd.DataFrame]):
        self.extract_features(df, feature_function)
        self.save_features()

