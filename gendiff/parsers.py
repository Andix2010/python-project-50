import json


def read_file(file_path):
    with open(file_path) as f:
        if file_path.endswith('.json'):
            return json.load(f)

    