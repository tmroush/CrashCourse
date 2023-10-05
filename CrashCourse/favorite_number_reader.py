import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    print(f"I couldn't find {filename}.")
else:
    print(f"I know your favorite number! It's {number}.")
