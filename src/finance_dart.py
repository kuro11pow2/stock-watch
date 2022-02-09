import json
from src.request import Request
from src.finance import Finance

# https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS003&apiId=2019016
class FinanceDart(Finance):

    def __init__(self, corp_code, crtfc_key):
        super(FinanceDart, self).__init__(corp_code, crtfc_key, ".json", "https://opendart.fss.or.kr/api/")

    def company_info_raw(self):
        if self._company_info_raw is None:
            print(f'INFO: dart company_info_raw 조회 {self._corp_code=}')
            target = 'company'
            params = {'crtfc_key': self._cert_key , 'corp_code': self._corp_code}
            response = Request(self._url + target + self._return_type, params).response()
            self._company_info_raw = json.loads(response.text)

        return self._company_info_raw

    def stock_code(self):
        return self.company_info_raw()['stock_code']

    def corp_name(self):
        return self.company_info_raw()['corp_name']
    
    def main_account_info_raw(self, bsns_year, reprt_code):
        if self._main_account_info_raw is None:
            print(f'INFO: dart main_account_info_raw 조회 {self._corp_code=}, {bsns_year=}, {reprt_code=}')
            target = 'fnlttSinglAcnt'
            params = {'crtfc_key': self._cert_key , 'corp_code': self._corp_code, 'bsns_year': bsns_year, 'reprt_code': reprt_code}
            response = Request(self._url + target + self._return_type, params).response()
            self._main_account_info_raw = json.loads(response.text)

            if self._main_account_info_raw['status'] != '000':
                print('WARN: main_account_info 조회 불가')
                self._main_account_info_raw['list'] = ''

        return self._main_account_info_raw

    def main_acount_info(self, bsns_year, reprt_code):
        return self.main_account_info_raw(bsns_year, reprt_code)['list']

