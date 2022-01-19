# https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS003&apiId=2019016


from pprint import pprint
from src.corporation import Corporation
import sys, datetime


def main(cert_key):

    corp_code = '00126380'
    bsns_year = '2020'
    reprt_code = '11011'
    # 1분기보고서 : 11013
    # 반기보고서 : 11012
    # 3분기보고서 : 11014
    # 사업보고서 : 11011

    corp = Corporation(cert_key, corp_code, bsns_year, reprt_code)
    info_arr = corp.main_account_info()
    res = [*map(lambda x: (x['thstrm_dt'], x['fs_nm'], x['account_nm'], x['thstrm_amount']), info_arr)]
    pprint(res)

    return res


def table_to_markdown_str(table) -> str:
    return str(table)


if __name__ == "__main__":

    import os
    from src.issue import Issue

    ret = main(sys.argv[1])

    gh_token = os.environ['MY_GITHUB_TOKEN']
    repo_name = "kuro11pow2/stock-watch"
    title=str(datetime.datetime.now())
    body=table_to_markdown_str(ret)
    issue = Issue(repo_name, gh_token, title, body)

    issue.create_issue()