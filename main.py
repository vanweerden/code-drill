#!/usr/bin/env python3

import sys
from os import listdir
from os.path import isfile, join
import importlib.util
import keyboard


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


# SET WORKING DIRECTORY
working_dir = sys.argv[1]
indexfilename = "._index"

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

    print(prompt)
    print("Press any key to see solution")
    # BUG: This keyboard read is also applied to the (y/n) below
    keyboard.read_event()
    print("SOLUTION")
    print(solution)
    
    # If no problems left, notify user and exit
    index += 1
    print(f"problem_count: {problem_count}")

    print(f"index: {index}")
    if index >= problem_count:
        print("You've studied all the problems!")
        keep_studying = False
    else:
        # BUG: The above keyboard event seems to "count" here 
        res = input("Keep studying? (y/n)")
        keep_studying = res.lower() == 'y' or res.lower() == 'yes'
        if keep_studying:
            print ("==================")

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
