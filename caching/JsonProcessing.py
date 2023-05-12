import json


class JsonProcessing():
    def __init__(self, type:str) -> None:
        self.type = type

    def add_new_value(self, new_value: dict):
        with open('cachingStorage.json', 'r') as f:
            data = json.load(f)

        # Append a new phone number to the list
        data[self.type].append(new_value)

        # Write the modified data back to the file
        with open('cachingStorage.json', 'w') as f:
            json.dump(data, f)

    def eliminate_a_value(self, key, value):
         # Load the JSON data from the file
        with open('cachingStorage.json', 'r') as f:
            data = json.load(f)

        # Find the value in the JSON data and remove it
        for item in data:
            if item.get(key) == value:
                data.remove(item)

        # Save the modified JSON data back to the file
        with open('cachingStorage.json', 'w') as f:
            json.dump(data, f, indent=2)

    def check_exist_value(self, key):
        with open('cachingStorage.json', 'r') as f:
            data = json.load(f)

        # Find the value in the JSON data and remove it
        return key in data.keys()