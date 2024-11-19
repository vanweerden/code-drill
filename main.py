#!/usr/bin/env python3

import sys
import os
from os import listdir
from os.path import isfile, join
import importlib.util
import keyboard
import yaml
import time
from utilities import * 

verbose = True

# Helper functions (export to a utils file)
def clear_terminal_screen():
    # NOTE: This works for Linux. Windows works differently
    clear = lambda: os.system('clear')
    clear()

# GET LIST OF FILENAMES
options = {}
with open("config.yaml", 'r') as stream:
    options = yaml.safe_load(stream)
working_dir = options["root-directory"]
indexfilepath = f"{working_dir}/._index"

# INIT CHECKS
filenames = [f for f in listdir(working_dir) if isfile(join(working_dir, f)) and f != "._index"]
index_dict = initialise_config(indexfilepath, filenames)
prompts = get_ordered_prompts(index_dict)

# BEGIN STUDY LOOP
clear_terminal_screen()
print(prompts)

keep_studying = True
index = 0
problem_count = len(prompts)
while keep_studying:
    filename = prompts[index]
    filepath = f"{working_dir}/{filename}"
    spec = importlib.util.spec_from_file_location(f"module.{filename}", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    subject = getattr(module, 'subject', None)
    prompt = getattr(module, 'prompt', None)
    solution = getattr(module, 'solution', None)

    print("\n================ QUESTION ================\n")
    if verbose:
        print("DEBUG <filename>:", filename)

    print("Subject:", subject.upper())
    print(prompt)
    confirm_see_solution = input("\nPress any key to see solution")
    
    print("\n================ SOLUTION ================\n")
    print(solution)
    print("\n==========================================\n")
    
    # GET DIFFICULTY
    difficulty_input = input("How difficult was that? (1: easy, 2: so-so, 3: hard)" )
    while difficulty_input not in ["1", "2", "3"]:
        difficulty_input = input("That is not an option. Please enter 1 (easy), 2 (so-so), or 3 (hard)" )
    update_metadata(indexfilepath, filename, int(difficulty_input))

    # If no problems left, notify user and exit
    index += 1
    if index >= problem_count:
        print("You've studied all the problems!")
        keep_studying = False
    else:
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
