import json
from src.request import Request
from src.stock import Stock

class StockFsc(Stock):
    
    def __init__(self, stock_code, cert_key):
        super(StockFsc, self).__init__(stock_code, cert_key, "https://api.odcloud.kr/api/GetStockSecuritiesInfoService/v1/getStockPriceInfo")

    def stock_info_raw(self, params=None):
        """
        https://www.data.go.kr/iim/api/selectAPIAcountView.do
        금융위원회_주식시세정보

        Header{
            resultCode	string  (API 호출 결과의 상태 코드)
            resultMsg	string  (API 호출 결과의 상태)
        }

        Item_StockPriceInfo{
            basDt	    string  (YYYYMMDD 기준일자)
            srtnCd	    string  (종목 코드보다 짧으면서 유일성이 보장되는 코드(6자리))
            isinCd	    string  (현선물 통합상품의 종목 코드(12자리))
            itmsNm	    string  (종목의 명칭)
            mrktCtg	    string  (주식의 시장 구분 (KOSPI/KOSDAQ/KONEX 중 1))
            clpr	    number  (정규시장의 매매시간종료시까지 형성되는 최종가격)
            vs  	    number  (전일 대비 등락)
            fltRt	    number  (전일 대비 등락에 따른 비율)
            mkp 	    number  (정규시장의 매매시간개시후 형성되는 최초가격)
            hipr	    number  (하루 중 가격의 최고치)
            lopr	    number  (하루 중 가격의 최저치)
            trqu	    number  (체결수량의 누적 합계)
            trPrc	    number  (거래건 별 체결가격 * 체결수량의 누적 합계)
            lstgStCnt	number  (종목의 상장주식수)
            mrktTotAmt	number  (종가 * 상장주식수)
        }
        """
        if self._stock_info_raw is None:
            print(f'INFO: fsc stock_info_raw 조회 {self.stock_code()=}')
            if params == None:
                params = {'serviceKey': self._cert_key, 
                            'resultType': 'json', 
                            'likeSrtnCd': self.stock_code()}

            response = Request(self._url, params).response()
            self._stock_info_raw = json.loads(response.text)
        
        return self._stock_info_raw

    def stock_info_list(self):
        if self._stock_info_list is None:
            self._stock_info_list = self.stock_info_raw()['response']['body']['items']['item']

        return self._stock_info_list

    def stock_price_close(self):
        recent = self.stock_info_list()[0]
        return (recent['basDt'], recent['clpr'])

