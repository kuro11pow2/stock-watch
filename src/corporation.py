
import requests, json


class corporation:

    def __init__(self, crtfc_key, corp_code, bsns_year, reprt_code, return_type='json'):
        self._url = 'https://opendart.fss.or.kr/api/'
        self._cert_key = crtfc_key
        self._corp_code = corp_code
        self._business_year = bsns_year
        self._report_code = reprt_code

        if return_type == 'json':
            self._return_type = '.json'
        elif return_type == 'xml':
            self._return_type = '.xml'
        else:
            raise Exception('wrong return type')
        
        self.info = None
    
    def main_account(self):
        if self.info is None:
            target = 'fnlttSinglAcnt'
            params = self._request_params()
            response = requests.get(url=self._url + target + self._return_type, params=params)
            self.info = json.loads(response.text)

        return self.info

    def clear_cache(self):
        self.info = None

    def _request_params(self):
        return {'crtfc_key': self._cert_key , 'corp_code': self._corp_code, 'bsns_year': self._business_year, 'reprt_code': self._report_code}
