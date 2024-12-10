import yaml
from datetime import datetime

class CardIndex():
    def __init__(self, path, file_names):
        self.index_dict = {}
        self.file_list = file_names
        self.index_filepath = path

        try:
            with open(self.index_filepath, 'r') as file:
                self.index_dict = yaml.safe_load(file) or {}
        except FileNotFoundError:
            # TODO: Create new file? 
            self.index_dict = {}

        self.add_new_files()
        self.remove_missing_files()
    
    def add_new_files(self):
        for filename in self.file_list:
            if filename not in self.index_dict:
                self.index_dict[filename] = {
                    'last_seen': None,
                    'ease': None,
                    'completion_count': 0
                }

        with open(self.index_filepath, 'w') as index_file:
            yaml.dump(self.index_dict, index_file, default_flow_style=False, sort_keys=False)

    def remove_missing_files(self):
        # Iterate over index file
        for filename in self.index_dict:
            if filename not in self.file_list:
                # TODO: Actually remove file
                print(f"Couldn't find {filename} file")

    def update_card(self, filename, ease_rating):
        completion_count = self.index_dict[filename].get("completion_count", 0) + 1
        previous_ease = self.index_dict[filename].get("ease", None)
        if previous_ease == None:
            previous_ease = ease_rating

        updated_ease = int(round((float(previous_ease) + float(ease_rating)) / 2, 0))

        self.index_dict[filename]["last_seen"] = datetime.now()
        self.index_dict[filename]["completion_count"] = completion_count
        self.index_dict[filename]["ease"] = updated_ease

        self.write_to_file()

    def write_to_file(self):
        with open(self.index_filepath, 'w') as index_file:
            yaml.dump(self.index_dict, index_file, default_flow_style=False, sort_keys=False)
