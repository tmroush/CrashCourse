person = {
    'first_name': 'phil',
    'last_name': 'roush',
    'city': 'aurora',
    'age': 56,
    'birth_place': 'tulsa'
}

for person_info in person:
    print(person[person_info])

# To get keys and values
for key, value in person.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print("\n")
# To get just keys:
for key in person.keys():
    print(key);
