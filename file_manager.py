import json


def save_variables(variables, filename):
    with open(filename, 'w') as f:
        json.dump(variables, f)


def load_variables(filename):
    with open(filename, 'r') as f:
        return json.load(f)
