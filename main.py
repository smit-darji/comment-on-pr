import os
from github import Github
from file_name_validator import remove_files_ofcompletely_ignored_directory, get_invalid_file_names, get_invalid_directory_names
from github_actions import post_pr_comment

CHANGED_FILE_NAMES = (os.environ.get('CHANGED_FILES'))
CHANGED_FILE_NAMES = CHANGED_FILE_NAMES.split(" ")
# print("changed_file_list :", CHANGED_FILE_NAMES)

# FILE_NAMES_TO_IGNORE = (os.environ.get('FILE_NAMES_TO_IGNORE'))
# DIRECTORY_NAMES_TO_COMPLETELY_IGNORE = (os.environ.get('DIRECTORY_NAMES_TO_COMPLETELY_IGNORE'))
# DIRECTORY_NAMES_TO_IGNORE = (os.environ.get('DIRECTORY_NAMES_TO_IGNORE'))
GITHUB_TOKEN = (os.environ.get('GITHUB_TOKEN'))
# CHANGED_FILE_NAMES = ['./.github/workflows/1.yml', './.github/workflows/script/file_name_validation.sh', './.github/workflows/test.yml', './ABCD/xyz/1234_YOGESH_TEST_12T.py', './ABCD/xyz/1234_YOGESH_TEST_12T.txt']
FILE_NAMES_TO_IGNORE = ["README.md", ".gitignore", "dist", "images"]
DIRECTORY_NAMES_TO_COMPLETELY_IGNORE = [".github", "Terraform",".gitignore"]
DIRECTORY_NAMES_TO_IGNORE = ['changes', 'terraform', 'terraform-master']

file_names_to_verify = remove_files_ofcompletely_ignored_directory(CHANGED_FILE_NAMES, DIRECTORY_NAMES_TO_COMPLETELY_IGNORE)

# invalid_file_names = get_invalid_file_names(file_names_to_verify, FILE_NAMES_TO_IGNORE)

# invalid_directory_names = get_invalid_directory_names(file_names_to_verify, DIRECTORY_NAMES_TO_IGNORE)
def in_fine (invalid_file_names, invalid_directory_names):
    invalid_file_names = get_invalid_file_names(file_names_to_verify, FILE_NAMES_TO_IGNORE)

    invalid_directory_names = get_invalid_directory_names(file_names_to_verify, DIRECTORY_NAMES_TO_IGNORE)
    print("In function",invalid_file_names) 
    print("In function",invalid_directory_names) 

if invalid_file_names :      
    github_client = Github(GITHUB_TOKEN)
    post_pr_comment(github_client, invalid_file_names, invalid_directory_names)
    exit(1)    
elif invalid_directory_names:
    exit(1)
else:
    github_client = Github(GITHUB_TOKEN)
    post_pr_comment(github_client, invalid_file_names, invalid_directory_names)