
from pprint import pformat, pprint
from src.corporation import Corporation
import sys, datetime


def finance_test(corp: Corporation):

    # 1분기보고서 : 11013
    # 반기보고서 : 11012
    # 3분기보고서 : 11014
    # 사업보고서 : 11011

    bsns_year = '2020'
    reprt_code = '11011'

    print("-------[ finance 테스트 ]-------")
    pprint(f'{corp.company_info_raw()=}')
    pprint(f'{corp.corp_name()=}')
    pprint(f'{corp.stock_code()=}')
    
    pprint(f'{corp.main_account_info_raw(bsns_year, reprt_code)=}')


def stock_test(corp: Corporation):
    print("-------[ stock 테스트 ]-------")
    pprint(f'{corp.stock_info_raw()=}')
    pprint(f'{corp.stock_info_list()=}')
    pprint(f'{corp.stock_price_close()=}')


def table_to_markdown_str(table) -> str:
    return str(table)


def main(dart_key, stock_key):
    corp_code_list = sorted(['00261443', '00760971', '00904672', '01152470', '01010110', '01137383', '01008762'])
    res = []

    for corp_code in corp_code_list:
        corp = Corporation(corp_code, dart_key, stock_key)
        # finance_test(corp)
        # stock_test(corp)
        res.append((corp.corp_code(), corp.corp_name(), corp.stock_code(), corp.stock_price_close()))

    return res


if __name__ == "__main__":

    import os
    from src.issue import Issue

    dart_key = sys.argv[1]
    stock_key = sys.argv[2]

    issue_body_str = pformat(main(dart_key, stock_key))

    repo_name = "kuro11pow2/stock-watch"
    gh_token = os.environ['MY_GITHUB_TOKEN']
    title=str(datetime.datetime.now())
    body=issue_body_str
    issue = Issue(repo_name, gh_token, title, body)

    issue.create_issue()