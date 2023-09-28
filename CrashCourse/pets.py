def describe_pet(owner_name, pet_type, pet_name):
    """Displays information about a pet"""
    print(f"\n{owner_name.title()} has a {pet_type}.")
    print(f"The {pet_type}'s name is {pet_name.title()}.")

pet_1 = {
    'owner_first': 'tricia',
    'owner_last': 'roush',
    'pet_type': 'dog',
    'pet_name': 'chloe',
    'pet_age': 12,
}

pet_2 = {
    'owner_first': 'becky',
    'owner_last': 'smith',
    'pet_type': 'dog',
    'pet_name': 'sammy',
    'pet_age': 12,
}

pet_3 = {
    'owner_first': 'john',
    'owner_last': 'gardenhire',
    'pet_type': 'dog',
    'pet_name': 'micki',
    'pet_age': 8,
}

pet_4 = {
    'owner_first': 'john',
    'owner_last': 'gardenhire',
    'pet_type': 'dog',
    'pet_name': 'curly',
    'pet_age': 11,
}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    owner_full_name = f"{pet['owner_first']} {pet['owner_last']}"
    describe_pet(owner_full_name, pet['pet_type'], pet['pet_name'])
    # print(f"\nThe owner is {pet['owner_first'].title()} {pet['owner_last'].title()}")
    # print(f"Their {pet['pet_type']}'s name is {pet['pet_name'].title()}.")
    if pet['pet_age'] > 8:
        print(f"{pet['pet_name'].title()} is considered a senior pet.")
    else:
        print(f"{pet['pet_name'].title()} is still considered young.")

