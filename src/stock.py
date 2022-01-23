import requests, json

class Stock:

    def __init__(self, stock_code, cert_key):
        self._url = "https://api.odcloud.kr/api/GetStockSecuritiesInfoService/v1/getStockPriceInfo"
        self._stock_code = stock_code
        self._cert_key = cert_key
        self._stock_price = None

    def stock_price(self):
        if self._stock_price is None:
            print(f'\n[stock 조회 {self._stock_code=}]')
            params = {'serviceKey': self._cert_key , 'resultType': 'json', 'likeSrtnCd': self._stock_code}
            response = requests.get(url=self._url, params=params)

            self._stock_price = json.loads(response.text)

        return self._stock_price['response']['body']['items']['item']

    def clear_cache(self):
        self.__init__(self._stock_code, self._cert_key)