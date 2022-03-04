import numpy as np
import pandas as pd
from numbers import Number

from strategy import Strategy, SmaCross
from utils import read_file, assert_msg, crossover, SMA

class ExchangeAPI:
    def __init__(self, data, cash, commission):
        assert_msg(0 < cash, 'The initial cash number should be greater than 0')
        assert_msg(0 <= commission <= 0.05, 'The commission should be between 0 and 0.05')
        self._initial_cash = cash
        self._data = data
        self._commission = commission
        self._position = 0
        self._cash = cash
        self._i = 0


    @property
    def cash(self):
        return self._cash
    
    @property
    def position(self):
        return self._position
    
    @property
    def initial_cash(self):
        return self._initial_cash

    def market_value(self):
        return self._cash + self._position 
    
