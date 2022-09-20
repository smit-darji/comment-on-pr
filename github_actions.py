import imp
import json
from lib2to3.pytree import type_repr
from operator import index
import os

from github import Github
# from main import invalid_file_names

def read_json(filepath):
    """
    Read a json file as a dictionary.

    Parameters
    ----------
    filepath : str

    Returns
    -------
    data : dict

    """
    with open(filepath, 'r') as f:
        return json.load(f)


def get_actions_input(input_name):
    """
    Get a Github actions input by name.

    Parameters
    ----------
    input_name : str

    Returns
    -------
    action_input : str

    Notes
    -----
    GitHub Actions creates an environment variable for the input with the name:

    INPUT_<CAPITALIZED_VARIABLE_NAME> (e.g. "INPUT_FOO" for "foo")

    References
    ----------
    .. [1] https://help.github.com/en/actions/automating-your-workflow-with-github-actions/metadata-syntax-for-github-actions#example  # noqa: E501

    """
    return os.getenv('INPUT_{}'.format(input_name).upper())


def load_template(filename):
    """
    Load a template.

    Parameters
    ----------
    filename : template file name

    Returns
    -------
    template : str

    """
    filename = "template.md"
    print("file is:",filename)
    print(type(filename))
    template_path = os.path.join('.github/workflows', filename)
    with open(template_path, 'r') as f:
        return f.read()



def post_pr_comment (github_client, invalid_file_names, invalid_directory_names):
    print("invalid_file_names" ,invalid_file_names)
    print("invalid_directory_names" ,invalid_directory_names)
    invalid_file_names_Stirng = ", ".join( invalid_file_names )
    invalid_directory_names_Stirng = ", ".join( invalid_directory_names )
        # search a pull request that triggered this action
    gh = Github(os.getenv('GITHUB_TOKEN'))
    event = read_json(os.getenv('GITHUB_EVENT_PATH'))
    branch_label = event['pull_request']['head']['label']  # author:branch
    branch_name = branch_label.split(':')[-1]
    repo = gh.get_repo(event['repository']['full_name'])
    prs = repo.get_pulls(state='open', sort='created', head=branch_label)
    pr = prs[0]
 
    filenamevalidation = invalid_file_names_Stirng
    dirname = invalid_directory_names_Stirng
    # load template
    template = load_template(get_actions_input('filename'))
    # for file_names in invalid_file_names:
    #   for dir_names in invalid_directory_names:
    #     print(file_names)
    pr_info = {
      'filenamevalidation':filenamevalidation,
      'dirname': dirname
    }
    print(type(pr_info))
    new_comment = template.format(**pr_info)

    # check if this pull request has a duplicated comment
    old_comments = [c.body for c in pr.get_issue_comments()]
    if new_comment in old_comments:
        new_comment = template.format(**pr_info)
        print('This pull request already a duplicated comment.')
        exit(0)

    # add the comment
    pr.create_issue_comment(new_comment)















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