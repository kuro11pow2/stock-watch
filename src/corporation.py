
import requests, json


class Corporation:

    def __init__(self, crtfc_key, corp_code, bsns_year, reprt_code):
        self._url = 'https://opendart.fss.or.kr/api/'
        self._cert_key = crtfc_key
        self._corp_code = corp_code
        self._business_year = bsns_year
        self._report_code = reprt_code
        self._return_type = '.json'
        self._main_account_info = None
    
    def main_account_info(self):
        if self._main_account_info is None:
            target = 'fnlttSinglAcnt'
            params = self._request_params()
            response = requests.get(url=self._url + target + self._return_type, params=params)
            self._main_account_info = json.loads(response.text)

        return self._main_account_info['list']

    def clear_cache(self):
        self.__init__(self._cert_key, self._corp_code, self._business_year, self._report_code)

    def _request_params(self):
        return {'crtfc_key': self._cert_key , 'corp_code': self._corp_code, 'bsns_year': self._business_year, 'reprt_code': self._report_code}
