import json

import yaml


def read_file(file_path):
    file_path = str(file_path)
    with open(file_path) as f:
        if file_path.endswith('.json'):
            return json.load(f)
        if file_path.endswith(('.yml', '.yaml')):
            return yaml.safe_load(f)
    raise ValueError(f"Unsupported file format: {file_path}")

    