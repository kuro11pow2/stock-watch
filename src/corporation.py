
from src.dart import Dart
from src.stock import Stock

TMP_YEAR = '2020'
TMP_REPRT_CODE = '11011'

class Corporation:

    def __init__(self, dart_corp_code, dart_cert_key, open_stock_price_key):
        self._corp_code = dart_corp_code
        self._dart_cert_key = dart_cert_key
        self._open_stock_price_key = open_stock_price_key

        self._dart = None
        self._stock = None

    def corp_code(self):
        return self._corp_code

    def stock_code(self):
        return self.dart().company_info()['stock_code']
    
    def corp_name(self):
        return self.dart().company_info()['corp_name']

    def dart(self):
        if self._dart == None:
            self._dart = Dart(self.corp_code(), self._dart_cert_key)

        return self._dart

    def stock(self):
        if self._stock == None:
            self._stock = Stock(self.stock_code(), self._open_stock_price_key)

        return self._stock
        
    def main_account_info(self, bsns_year, reprt_code):
        return self.dart().main_account_info(bsns_year, reprt_code)

    def stock_price(self):
        return self.stock().stock_price()
