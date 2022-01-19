
# https://github.com/PyGithub/PyGithub
from github import Github

class Issue:

    def __init__(self, repo_name, gh_token, title, body):
        """
        repo_name: ex. "kuro11pow2/stock-watch"
        """
        self.repo_name = repo_name
        self.gh_token = gh_token
        self.title = title
        self.body = body

    def create_issue(self):

        g = Github(self.gh_token)
        repo = g.get_repo(self.repo_name)

        repo.create_issue(title=self.title, body=self.body)

