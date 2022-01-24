# https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS003&apiId=2019016


from pprint import pprint
from src.corporation import Corporation
import sys, datetime

def dart_demo(corp: Corporation):
    
    # 1분기보고서 : 11013
    # 반기보고서 : 11012
    # 3분기보고서 : 11014
    # 사업보고서 : 11011
    reprt_code = '11011'
    bsns_year = '2020'

    info_arr = corp.main_account_info(bsns_year, reprt_code)

    # info_arr = [*map(lambda x: (x['thstrm_dt'], x['fs_nm'], x['account_nm'], x['thstrm_amount']), info_arr)]
    pprint(info_arr)

    return info_arr


def stock_demo(corp: Corporation):
    
    info_arr = corp.stock_price()
    pprint(info_arr)

    return info_arr


def table_to_markdown_str(table) -> str:
    return str(table)


def main(dart_key, stock_key):
    corp_code_list = sorted(['00261443', '00760971', '00904672', '01152470', '01010110', '01137383', '01008762'])
    res = []

    for corp_code in corp_code_list:
        corp = Corporation(corp_code, dart_key, stock_key)
        res.append((corp.corp_code(), corp.corp_name(), corp.stock_code()))

    return res


if __name__ == "__main__":

    import os
    from src.issue import Issue

    dart_key = sys.argv[1]
    stock_key = sys.argv[2]

    issue_body_str = str(main(dart_key, stock_key))

    repo_name = "kuro11pow2/stock-watch"
    gh_token = os.environ['MY_GITHUB_TOKEN']
    title=str(datetime.datetime.now())
    body=issue_body_str
    issue = Issue(repo_name, gh_token, title, body)

    issue.create_issue()