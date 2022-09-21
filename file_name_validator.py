import re
import logging

def remove_files_ofcompletely_ignored_directory (changed_file_list, directory_names_to_ignore_completely):
    file_names_to_verify = []
    for file_path in changed_file_list:
        is_file_ignorable = True
        for dir_path in directory_names_to_ignore_completely:
            if file_path.startswith('./' + dir_path):
                is_file_ignorable = False
        if is_file_ignorable:
            file_names_to_verify.append(file_path)
    return file_names_to_verify

def get_invalid_file_names(file_names_to_verify, file_names_to_ignore):
    invalid_file_names = []
    unique_file_names=[]
    
    for file_path in file_names_to_verify:
        file_name = file_path.rsplit('/', 1)[-1]
        if file_name not in unique_file_names and file_name not in file_names_to_ignore:
            unique_file_names.append(file_name)
    
    for file_name in unique_file_names:
        match = re.search("[0-9]{4}_[A-Z0-9_]*.[a-zA-Z]*$", file_name)
        if match:
            logging.info("%s is a valid filename:", file_name)
        else:
            logging.error("%s is not a valid filename:", file_name)
            invalid_file_names.append(file_name)
    
    return invalid_file_names

def get_invalid_directory_names(file_names_to_verify, directory_names_to_ignore):
    invalid_directory_names = []
    unique_directory_names=[]

    for file_path in file_names_to_verify:
        dir_name_list = file_path.rsplit('/')[1:-1]
        for dir_name in dir_name_list:
            if dir_name not in unique_directory_names and dir_name not in directory_names_to_ignore:
                unique_directory_names.append(dir_name)
    
    for dir_name in unique_directory_names:
        match = re.search("[0-9]{4}_[A-Z0-9_]*.[a-zA-Z]*$", dir_name)
        if match:
            logging.info("%s is a valid directory name:", dir_name)
        else:
            logging.error("%s is not a valid directory name:", dir_name)
            invalid_directory_names.append(dir_name)
    return invalid_directory_names
