# from github import Github
# from main import GITHUB_TOKEN

# def post_pr_comment (github_client, invalid_file_names, invalid_directory_names):
#   print(invalid_file_names)
#   print(invalid_directory_names)
#   # g = Github("access_token")
#   gh = Github(GITHUB_TOKEN)
#   repo = gh.repository("smit-darji", "comment-on-pr")
#   pr = repo.create_pull("description", base, from_branch, detailed)
#   issue = repo.issue(pr.number)
#   issue.create_comment("test :",invalid_file_names)

from github import Github

# First create a Github instance:

# using an access token
g = Github("access_token")

# Github Enterprise with custom hostname
g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)