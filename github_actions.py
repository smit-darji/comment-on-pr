from github import Github
from main import GITHUB_TOKEN

def post_pr_comment (github_client, invalid_file_names, invalid_directory_names):
  print(invalid_file_names)
  print(invalid_directory_names)
  # g = Github("access_token")
  gh = Github(GITHUB_TOKEN)
  repo = gh.repository(user, repo_name)
  pr = repo.create_pull(description, base, from_branch, detailed)
  issue = repo.issue(pr.number)
  issue.create_comment("test :",invalid_file_names)