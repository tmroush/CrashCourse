import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    while True:
        number = input("What is your favorite number? ")
        if number.isdecimal():
            break
        else:
            print("That is not a number, please try again.")

    with open(filename, 'w') as f:
        json.dump(number, f)
else:
    print(f"I know your favorite number! It's {number}.")