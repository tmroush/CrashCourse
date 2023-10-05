import json

while True:
    number = input("What is your favorite number? ")
    if number.isdecimal():
        break
    else:
        print("That is not a number, please try again.")

filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(number, f)
