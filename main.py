#!/usr/bin/env python3

import sys
import os
import importlib.util
import keyboard
import yaml
import time
from utilities import * 

verbose = True

# INITTIALISE
working_dir = get_working_directory()
indexfilepath = f"{working_dir}/._index"

prompts = get_prompts(working_dir)

clear_terminal_screen()

# BEGIN STUDY LOOP
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
    difficulty_input = input("How difficult was that? (0: impossible, 1: errors, 2: so-so, 3: easy) ")
    while difficulty_input not in ["0", "1", "2", "3"]:
        difficulty_input = input("That is not an option. Please enter 0 (impossible), 1 (errors), 2 (so-so), or 3 (easy)" )
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

