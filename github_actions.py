from github import Github


def post_pr_comment (github_client, invalid_file_names, invalid_directory_names):
  print("action file ",invalid_file_names)
  print("Action dir",invalid_directory_names)
  # g = Github("access_token")
  # gh = Github(GITHUB_TOKEN)
  # for repo in gh.get_user().get_repos():
  #     print(repo.name)

# from github import Github
# from main import GITHUB_TOKEN

# # First create a Github instance:

# # using an access token
# g = Github(GITHUB_TOKEN)

# # Github Enterprise with custom hostname

# # Then play with your Github objects:
# for repo in g.get_user().get_repos():
#     print(repo.name)