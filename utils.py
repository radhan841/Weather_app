import os
import pandas as pd


def get_weather_data(path):
    if os.path.isfile(path):
        return pd.read_csv(path, sep='\t', names=['date', 'max_temp', 'min_temp', 'precipitation'])


def get_crop_data(path):
    if os.path.isfile(path):
        return pd.read_csv(path, sep='\t', names=['year', 'yield_per_year'])
