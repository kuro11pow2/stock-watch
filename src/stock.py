import requests, json

class Stock:

    def __init__(self, stock_code, cert_key):
        self._url = "https://api.odcloud.kr/api/GetStockSecuritiesInfoService/v1/getStockPriceInfo"
        self._stock_code = stock_code
        self._cert_key = cert_key

    def stock_price(self):
        params = {'serviceKey': self._cert_key , 'resultType': 'json', 'likeSrtnCd': self._stock_code}
        response = requests.get(url=self._url, params=params)

        res = json.loads(response.text)

        return res