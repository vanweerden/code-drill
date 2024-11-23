import yaml
from datetime import datetime
import random
import os
from os import listdir
from os.path import isfile, join
from enum import Enum

def initialise_config(index_filepath, file_list):
    try:
        with open(index_filepath, 'r') as file:
            index_dict = yaml.safe_load(file) or {}
    except FileNotFoundError:
        index_dict = {}

    current_date = datetime.now().strftime('%Y-%m-%d')

    # Add new files
    for filename in file_list:
        if filename not in index_dict:
            index_dict[filename] = {
                'last_seen': None,
                'difficulty': None,
                'completion_count': 0
            }


    with open(index_filepath, 'w') as index_file:
        yaml.dump(index_dict, index_file, default_flow_style=False, sort_keys=False)
    
    return index_dict

def update_metadata(index_filepath, filename, rating_input):
    try:
        with open(index_filepath, 'r') as file:
            index_dict = yaml.safe_load(file) or {}
    except FileNotFoundError:
        index_dict = {}
    
    # Convert difficulty from 1, 2, 3 to 
    input_to_ease_map = {
        0: 0, # "Impossible"
        1: 1, # "Errors"
        2: 5, # "So-so"
        3: 10, # "Easy"
    }

    completion_count = index_dict[filename].get("completion_count", 0) + 1
    current_rating = input_to_ease_map[rating_input]
    previous_ease = index_dict[filename].get("difficulty", None)
    if previous_ease == None:
        previous_ease = current_rating

    updated_ease = int(round((float(previous_ease) + float(current_rating)) / 2, 0))

    index_dict[filename]["last_seen"] = datetime.now()
    index_dict[filename]["completion_count"] = completion_count
    index_dict[filename]["ease"] = updated_ease

    with open(index_filepath, 'w') as index_file:
        yaml.dump(index_dict, index_file, default_flow_style=False, sort_keys=False)

class CardCategory(Enum):
    NEW = 0
    HARD = 1
    NORMAL = 2

def card_sort_key(card):
    '''Returns a tuple containing key for sorting cards.'''
    is_new = card[1]["last_seen"] is None
    last_seen = datetime.min if is_new else card[1]["last_seen"]
    ease = 5 if card[1]["ease"] is None else card[1]["ease"]

    category = CardCategory.NEW.value if is_new else CardCategory.HARD.value if ease < 5 else CardCategory.NORMAL.value

    return (category, ease, last_seen)

def get_prompts(working_dir):
    indexfilepath = f"{working_dir}/._index"
    filenames = [f for f in listdir(working_dir) if isfile(join(working_dir, f)) and f != "._index"]
    index_dict = initialise_config(indexfilepath, filenames)
    return list(dict(sorted(index_dict.items(), key=card_sort_key)))

def clear_terminal_screen():
    # NOTE: This works for Linux. Windows works differently
    clear = lambda: os.system('clear')
    clear()

def get_working_directory():
    options = {}
    with open("config.yaml", 'r') as stream:
        options = yaml.safe_load(stream)
    return options["root-directory"]