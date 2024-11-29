# Code Drill
Code Drill is a CLI Python program for drilling coding problems. It's basically a rudimentary flashcard system for writing code. 

I am currently studying compsci and a lot of my study time is spent working on practice problems. This program is meant to help automate this process, and I am continually improving Code Drill to help me study for me compsci degree. 

## Installation
1. Copy config-sample.yaml file as config.yaml 
2. Update the "root-directory" setting to point to the root path where your prompts will be stored

## Usage
1. Add prompt files to the root-directory folder set up in the config. A prompt file is a Python file with four variables. For example:

```Python
subject = "python"
prompt = "Write a program that asks the user their age (in years), and then tells them approximately how many days that is."
solution = '''
age_input = input("Enter your age in years: ")
age_in_years = int(age_input)
age_in_days = age_in_years * 365
print("You are approx.", age_in_days, "days old")
'''
notes = "Input will be a string, so you need to convert it to an int"

```
2. Run main.py

## Roadmap
Ideas for future improvements:
- Draw cards from multiple folders
- Option to study specific subjects
- Writing answers to code in-terminal
- Automated testing of written solutions
- Come up with a better name

## License

[MIT](https://choosealicense.com/licenses/mit/)
