#!/usr/bin/env python3

import sys
import os
from os import listdir
from os.path import isfile, join
import keyboard
import yaml
import time
import random
from enum import Enum
from CardIndex import CardIndex
from Card import Card

verbose = True

class CardCategory(Enum):
    NEW = 0
    HARD = 1
    NORMAL = 2

def get_working_directory():
    options = {}
    with open("config.yaml", 'r') as stream:
        options = yaml.safe_load(stream)
    return options["root-directory"]

def clear_terminal_screen():
    # NOTE: This works for Linux. Windows works differently
    clear = lambda: os.system('clear')
    clear()

def card_sort_key(card):
    '''Returns a tuple containing key for sorting cards.'''
    is_new = card[1]["last_seen"] is None or card[1]["ease"] is None
    last_seen = datetime.min if is_new else card[1]["last_seen"]
    ease = 5 if card[1]["ease"] is None else card[1]["ease"]

    category = CardCategory.NEW.value if is_new else CardCategory.HARD.value if ease < 5 else CardCategory.NORMAL.value

    return (category, ease, last_seen)

def main():
    # INITTIALISE
    working_dir = get_working_directory()
    indexfilepath = f"{working_dir}/._index"
    filenames = [f for f in listdir(working_dir) if isfile(join(working_dir, f)) and f != "._index"]
    
    card_index = CardIndex(indexfilepath, filenames)

    # TODO: Combine these (ust need to sort cards)
    prompts = list(dict(sorted(card_index.index_dict.items(), key=card_sort_key)))
    cards = [Card(os.path.join(working_dir, file)) for file in filenames]

    # BEGIN STUDY LOOP
    keep_studying = True
    index = 0
    problem_count = len(prompts)
    if problem_count == 0:
        print(f"No cards found in {working_dir}")
        return -1

    clear_terminal_screen()
    while keep_studying:
        filename = prompts[index]
        card = list(filter(lambda c: c.filename == filename, cards))[0]

        print("\n================ QUESTION ================\n")
        if verbose:
            print("DEBUG <filename>:", filename)

        print("Subject:", card.subject.upper())
        # TODO: Print difficulty here
        print(card.prompt)
        confirm_see_solution = input("\nPress any key to see solution")
        
        print("\n================ SOLUTION ================\n")
        print(card.solution)
        print("\n==========================================\n")
        
        # GET DIFFICULTY
        difficulty_input = input("How difficult was that? (0-10 where 0 is impossible and 10 is trivial) ")
        while not difficulty_input.isnumeric() or int(difficulty_input) not in range(0,11):
            difficulty_input = input("That is not an option. Please a number between 1 and 10 (0: impossible and 10: trivial))" )
        card_index.update_card(filename, int(difficulty_input))

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

if __name__ == '__main__':
    main()