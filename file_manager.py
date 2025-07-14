import json

VARIABLES_FILE = "variables.json"


def save_variables(variables):
    with open(VARIABLES_FILE, 'w') as f:
        json.dump(variables, f)


def load_variables():
    try:
        with open(VARIABLES_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
