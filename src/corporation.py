
from src.finance import Finance
from src.stock import FscStock

TMP_YEAR = '2020'
TMP_REPRT_CODE = '11011'

class Corporation:

    def __init__(self, finance_corp_code, finance_cert_key, open_stock_price_key):
        self._corp_code = finance_corp_code
        self._finance_cert_key = finance_cert_key
        self._open_stock_price_key = open_stock_price_key

        self._finance = None
        self._stock = None

    def corp_code(self):
        return self._corp_code

    def finance(self):
        if self._finance == None:
            self._finance = Finance(self.corp_code(), self._finance_cert_key)

        return self._finance

    def stock(self):
        if self._stock == None:
            self._stock = FscStock(self.stock_code(), self._open_stock_price_key)

        return self._stock

    def company_info_raw(self):
        return self.finance().company_info_raw()

    def stock_code(self):
        return self.finance().company_info_raw()['stock_code']
    
    def corp_name(self):
        return self.finance().company_info_raw()['corp_name']
        
    def main_account_info_raw(self, bsns_year, reprt_code):
        return self.finance().main_account_info_raw(bsns_year, reprt_code)
    
    def stock_info_raw(self):
        return self.stock().stock_info_raw()

    def stock_info_list(self):
        return self.stock().stock_info_list()

    def stock_price_close(self):
        return self.stock().stock_price_close()
