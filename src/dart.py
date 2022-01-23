from typing import List
import requests, json

class Dart:

    def __init__(self, corp_code, crtfc_key):
        self._url = 'https://opendart.fss.or.kr/api/'
        self._corp_code = corp_code
        self._cert_key = crtfc_key
        self._return_type = '.json'
        self._company_info = None
        self._main_account_info = None

    def company_info(self):
        if self._company_info is None:
            print(f'\n[dart company_info 조회 {self._corp_code=}]')
            target = 'company'
            params = {'crtfc_key': self._cert_key , 'corp_code': self._corp_code}
            response = requests.get(url=self._url + target + self._return_type, params=params)
            self._company_info = json.loads(response.text)

        return self._company_info
    
    def main_account_info(self, bsns_year, reprt_code):
        if self._main_account_info is None:
            print(f'\n[dart main_account_info 조회 {self._corp_code=}, {bsns_year=}, {reprt_code=}]')
            target = 'fnlttSinglAcnt'
            params = {'crtfc_key': self._cert_key , 'corp_code': self._corp_code, 'bsns_year': bsns_year, 'reprt_code': reprt_code}
            response = requests.get(url=self._url + target + self._return_type, params=params)
            self._main_account_info = json.loads(response.text)

        return self._main_account_info['list']

    def clear_cache(self):
        self.__init__(self._corp_code, self._cert_key)
