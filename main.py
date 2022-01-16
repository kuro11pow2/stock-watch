# https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS003&apiId=2019016


from pprint import pprint
from src.corporation import corporation
import sys


def main(cert_key):

    corp_code = '00126380'
    bsns_year = '2020'
    reprt_code = '11011'
    # 1분기보고서 : 11013
    # 반기보고서 : 11012
    # 3분기보고서 : 11014
    # 사업보고서 : 11011

    corp = corporation(cert_key, corp_code, bsns_year, reprt_code)
    info_arr = corp.main_account_info()
    pprint([*map(lambda x: (x['thstrm_dt'], x['fs_nm'], x['account_nm'], x['thstrm_amount']), info_arr)])


if __name__ == "__main__":
    
    main(sys.argv[1])