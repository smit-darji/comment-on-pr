from cgi import test
import imp
import json
import os
from entrypoint import read_json
from github import Github
# from github_actions import post_pr_comment
# from .validationmain import invalid_file_names
# import main

test='smit'
def post_pr_comment (github_client, invalid_file_names, invalid_directory_names):
    print("action file ",invalid_file_names)
    print("Action dir",invalid_directory_names)
    print(type(invalid_file_names))
    invalid_file_names_Stirng = " ".join( invalid_file_names )
    print(invalid_file_names_Stirng)
    print (type(invalid_file_names_Stirng))  
    gh = Github(os.getenv('GITHUB_TOKEN'))
    event = read_json(os.getenv('GITHUB_EVENT_PATH'))
    # branch_label = event['pull_request']['head']['label']  # author:branch
    # branch_name = branch_label.split(':')[-1]
    repo = gh.get_repo(event['repository']['full_name'])
    prs = repo.get_pulls(state='open', sort='created')
    pr = prs[0]
    # filenamevalidation = invalid_file_names_Stirng
    # # load template
    # template = load_template(get_actions_input('filename'))

    # # build a comment
    # pr_info = {
    #     'filenamevalidation':filenamevalidation,
    #     'pull_id': pr.number,
    #     'branch_name': branch_name
    # }
    # new_comment = template.format(**pr_info)

    # # check if this pull request has a duplicated comment
    # old_comments = [c.body for c in pr.get_issue_comments()]
    # if new_comment in old_comments:
    #     print('This pull request already a duplicated comment.')
    #     exit(0)

    # add the comment
    pr.create_issue_comment('invalid FILE NAME: ',invalid_file_names_Stirng)















  #g = Github("access_token")
  #gh = Github(GITHUB_TOKEN)
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