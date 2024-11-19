# Code Drill
A CLI Python program for drilling coding problems 

## Setup
1. Copy config-sample.yaml file as config.yaml 
2. Update the "root-directory" setting to point to the root path where your prompts will be stored

## Index File
- The .index.yaml file is the heart of this program. It's where metadata for each prompt file is stored. Here is an example:

```Yaml
newton_sqrrt.py: 
    last_seen: 2024-11-11 07:23:22.599678
    difficulty: 5
    completion_count: 0
```
- Difficulty is a float from 0.0 to 10.0: The greater the number, the greater the perceived difficulty. 
- The order of the prompts is determined by the date it was last seen and the perceived difficulty (harder prompts are shown more often)