#!/usr/bin/env python3

import sys
from os import listdir
from os.path import isfile, join
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

# INIT CHECKS

filelist = [f for f in listdir(working_dir) if isfile(join(working_dir, f))]

# Check for index file. If not, create it in working_directory
with open(f"{working_dir}/._index", 'w') as f:
    for f in filelist:
    # Add any new files to the .index JSON file
    # Update properties of each one if different

# GET PROBLEM LIST
# Read from index file 

# STUDY LOOP
# Loop until all problems have been seen in that session OR user selects to stop:
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
