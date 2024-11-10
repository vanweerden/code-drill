import yaml
from datetime import datetime
import random

def initialise_config(index_filepath, file_list):
    try:
        with open(index_filepath, 'r') as file:
            index_dict = yaml.safe_load(file) or {}
    except FileNotFoundError:
        index_dict = {}

    current_date = datetime.now().strftime('%Y-%m-%d')

    for filename in file_list:
        if filename not in index_dict:
            index_dict[filename] = None

    with open(index_filepath, 'w') as index_file:
        yaml.dump(index_dict, index_file, default_flow_style=False, sort_keys=False)
    
    return index_dict

def update_last_seen(index_filepath, filename):
    try:
        with open(index_filepath, 'r') as file:
            index_dict = yaml.safe_load(file) or {}
    except FileNotFoundError:
        index_dict = {}
    
    current_date = datetime.now()
    index_dict[filename] = current_date

    with open(index_filepath, 'w') as index_file:
        yaml.dump(index_dict, index_file, default_flow_style=False, sort_keys=False)

def get_ordered_prompts(index_dict):
    # Takes dictionary of files and returns sorted list of file names
    return list(dict(sorted(index_dict.items(), key=lambda item: (item[1] is not None, item[1]))).keys())