import json
from Interface.JsonInterface import JsonProcessingInterface


class JsonProcessing(JsonProcessingInterface):
    def __init__(self, attribute_name:str, filename: str) -> None:
        self.attribute_name = attribute_name
        self.filename = filename

    def add_new_value(self, new_value: dict):
        with open(self.filename, 'r') as f:
            data = json.load(f)

        # Append a new phone number to the list
        data[self.attribute_name].append(new_value)

        # Write the modified data back to the file
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def eliminate_a_value(self, key, value):
         # Load the JSON data from the file
        with open(self.filename, 'r') as f:
            data = json.load(f)

        # Find the value in the JSON data and remove it
        for item in data:
            if item.get(key) == value:
                data.remove(item)

        # Save the modified JSON data back to the file
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)

    def check_exist_value(self, key):
        with open(self.filename, 'r') as f:
            data = json.load(f)

        # Find the value in the JSON data and remove it
        return key in data.keys()