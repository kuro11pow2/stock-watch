
import os

# https://github.com/PyGithub/PyGithub
from github import Github


def create_issue(title, body):
    gh_token = os.environ['MY_GITHUB_TOKEN']
    repos_name = "kuro11pow2/stock-watch"

    g = Github(gh_token)
    repo = g.get_repo(repos_name)

    repo.create_issue(title=title, body=body)


