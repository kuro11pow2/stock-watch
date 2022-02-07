
from abc import ABCMeta
from abc import *

class Stock(metaclass=ABCMeta):

    def __init__(self, stock_code, cert_key, url):
        self._stock_code = stock_code
        self._stock_info_raw = None
        self._stock_info_list = None
        
        self._cert_key = cert_key
        self._url = url

    def stock_code(self):
        return self._stock_code

    @abstractmethod
    def stock_info_raw(self, params=None):
        pass

    @abstractmethod
    def stock_info_list(self):
        pass

    @abstractmethod
    def stock_price_close(self):
        pass