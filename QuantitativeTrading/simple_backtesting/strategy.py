import abc
import numpy as np
from typing import Callable

class Strategy(metaclass=abc.ABCMeta):
    def __init__(self, broker, data):
        self._indicators = []
        self._broker = broker
        self._data = data
        self._tick = 0
    
    def I(self, func: Callable, *args) -> np.ndarray:
        def init():
            self.sma = self.I(utils.SMA, self.data.Close, N)
        
        value = func(*args)
        value = np.asarray(value)
        assert_msg(value.shape[-1] == len(self._data.Close), 'The lengt of the indicator is not the same as the one for data')

        self._indicators.append(value)
        return value

    @property 
    def tick(self):
        return self._tick
    
    @abc.abstractmethod
    def init(self):
        pass
    
    @abc.abstractmethod
    def next(self, tick):
        pass

    def buy(self):
        self._broker.buy()
    
    def sell(self):
        self._broker.sell()
    
    @property
    def data(self):
        return self._data



from utils import assert_msg, crossover, SMA

class SmaCross(Strategy):
    fast = 30
    slow = 90

    def init(self):
        self.sma1 = self.I(SMA, self.data.Close, self.fast)
        self.sma2 = self.I(SMA, self.data.Close, self.slow)
    
    def next(self, tick):
        if crossover(self.sma1[:tick], self.sma2[:tick]):
            self.buy()
        elif crossover(self.sma2[:tick], self.sma1[:tick]):
            self.sell()
        else:
            pass