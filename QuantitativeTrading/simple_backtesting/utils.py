import os.path as path
import pandas as pd

def assert_msg(condition, msg):
    if not condition:
        raise Exception(msg)


def read_file(file_name):
    file_path = path.join(path.dirname(__file__), file_name)

    assert_msg(path.exists(file_path), 'File does not exist')

    return pd.read_csv(file_path, index_col=0, parse_dates=True, infer_datetime_format=True)

def SMA(values, n):
    return pd.Series(values).rolling(n).mean()

def crossover(series1, series2):
    return series1[-2] < series2[-2] and series1[-1] > series2[-1]