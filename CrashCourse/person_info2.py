phil = {
    'first_name': 'phil',
    'last_name': 'roush',
    'city': 'aurora',
    'age': 56,
    'birth_place': 'tulsa',
}

toni = {
    'first_name': 'toni',
    'last_name': 'roush',
    'city': 'quito',
    'age': 21,
    'birth_place': 'denver',
}

john = {
    'first_name': 'john',
    'last_name': 'gardenhire',
    'city': 'las cruces',
    'age': 79,
    'birth_place': 'miami',
}

people = [phil, toni, john]

for person in people:
    print(f"\nFull name: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"\tCity: {person['city'].title()}")
    print(f"\tAge: {person['age']}")
    print(f"\tBirth place: {person['birth_place'].title()}")
