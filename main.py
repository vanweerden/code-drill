#!/usr/bin/env python3

import sys
import os
from os import listdir
from os.path import isfile, join
import importlib.util
import keyboard
import yaml

'''
File structure: JSON with the following props
subject
prompt
solution
notes
'''

'''
Index file tracks metadata
JSON key-value where key is filename with props:
subject
path
last viewed
failcount
okcount
easycount
'''

# Helper functions (export to a utils file)
def clear_terminal_screen():
    # NOTE: This works for Linux. Windows works differently
    clear = lambda: os.system('clear')
    clear()


# SET WORKING DIRECTORY
stream = open("config.yaml", 'r')
options = yaml.load(stream, Loader=yaml.CLoader)
working_dir = options["root-directory"]
indexfilename = "._index"

print(working_dir)

filenames = [f for f in listdir(working_dir) if isfile(join(working_dir, f)) and f != "._index"]

# INIT CHECKS
# Check for index file. If not, create it in working_directory
# with open(f"{working_dir}/._index", 'w') as f:
#     for f in filelist:
    # Add any new files to the .index JSON file
    # Update properties of each one if different

# GET PROBLEM LIST
# Read from index file 

# STUDY LOOP
clear_terminal_screen()

keep_studying = True
index = 0
problem_count = len(filenames)
while keep_studying:
    filename = filenames[index]
    filepath = f"{working_dir}/{filename}"
    spec = importlib.util.spec_from_file_location(f"module.{filename}", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    prompt = getattr(module, 'prompt', None)
    solution = getattr(module, 'solution', None)

    print("\n================ QUESTION ================\n")
    print(prompt)
    # BUG: This keyboard read is also applied to the (y/n) below
    confirm_see_solution = input("\nPress any key to see solution")
    
    print("\n================ SOLUTION ================\n")
    print(solution)
    print("\n==========================================\n")
    
    # If no problems left, notify user and exit
    index += 1
    if index >= problem_count:
        print("You've studied all the problems!")
        keep_studying = False
    else:
        # BUG: The above keyboard event seems to "count" here 
        print(f"{problem_count - index+1} problems left")
        res = input("Press (n/N) to stop")
        keep_studying = res.lower() != 'n' and res.lower() != 'no'
        if keep_studying:
            clear_terminal_screen()
        else:
            break

# SELECT FILE
    # 
# PARSE FILE
# DISPLAY PROMPT
# USER INPUT:
    # Pass, Fail
    # Update last time file seen
    # Show solution and notes
# Prompt: "Continue?"
    # If no, kill loop
    # If yes, select next file in queue 
