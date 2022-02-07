from abc import ABCMeta
from abc import *

class Finance(metaclass=ABCMeta):

    def __init__(self, corp_code, crtfc_key, return_type, url):
        self._corp_code = corp_code
        self._return_type = return_type
        self._company_info_raw = None
        self._main_account_info_raw = None

        self._cert_key = crtfc_key
        self._url = url

    @abstractmethod
    def company_info_raw(self):
        pass

    @abstractmethod
    def stock_code(self):
        pass
    
    @abstractmethod
    def corp_name(self):
        pass
    
    @abstractmethod
    def main_account_info_raw(self, bsns_year, reprt_code):
        pass
