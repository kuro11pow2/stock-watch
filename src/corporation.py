
import requests, json
from src.dart import Dart
from src.stock import Stock

TMP_YEAR = '2020'
TMP_REPRT_CODE = '11011'

class Corporation:

    def __init__(self, dart_corp_code, dart_cert_key, open_stock_price_key):
        self.corp_code = dart_corp_code
        self.stock_code = None
        self.dart_cert_key = dart_cert_key
        self.open_stock_price_key = open_stock_price_key
    
    def main_account_info(self, bsns_year, reprt_code):
        res = Dart(self.corp_code, bsns_year, reprt_code, self.dart_cert_key).main_account_info()

        if self.stock_code == None and len(res) > 0:
            self.stock_code = res[0]['stock_code']

        return res

    def stock_price(self):
        if self.stock_code == None:
            res = Dart(self.corp_code, TMP_YEAR, TMP_REPRT_CODE, self.dart_cert_key).main_account_info()

            if len(res) > 0:
                self.stock_code = res[0]['stock_code']

        res = Stock(self.stock_code, self.open_stock_price_key).stock_price()

        return res
