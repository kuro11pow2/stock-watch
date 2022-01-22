# https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS003&apiId=2019016


from pprint import pprint
from src.corporation import Corporation
import sys, datetime
import requests, json

def dart_demo(corp: Corporation):
    
    # 1분기보고서 : 11013
    # 반기보고서 : 11012
    # 3분기보고서 : 11014
    # 사업보고서 : 11011
    reprt_code = '11011'
    bsns_year = '2020'

    info_arr = corp.main_account_info(bsns_year, reprt_code)
    res = [*map(lambda x: (x['thstrm_dt'], x['fs_nm'], x['account_nm'], x['thstrm_amount']), info_arr)]
    pprint(res)

    return res


def stock_demo(corp: Corporation):
    
    info_arr = corp.stock_price()
    pprint(info_arr)

    return info_arr


def main(corp_code, dart_key, stock_key):
    corp = Corporation(corp_code, dart_key, stock_key)

    ret = ''
    ret += dart_demo(corp) + '\n\n'
    ret += stock_demo(corp)

    return ret


def table_to_markdown_str(table) -> str:
    return str(table)


if __name__ == "__main__":

    import os
    from src.issue import Issue

    corp_code = sys.argv[1]
    dart_key = sys.argv[2]
    stock_key = sys.argv[3]

    ret = main(corp_code, dart_key, stock_key)

    gh_token = os.environ['MY_GITHUB_TOKEN']
    repo_name = "kuro11pow2/stock-watch"
    title=str(datetime.datetime.now())
    body=table_to_markdown_str(ret)
    issue = Issue(repo_name, gh_token, title, body)

    issue.create_issue()