cat_filename = 'cats.txt'
dog_filename = 'dogs.txt'

try:
    with open(cat_filename) as cat_file:
        cat_lines = cat_file.readlines()
except FileNotFoundError:
    '''print(f"File {cat_filename} not found.")'''
    pass
else:
    print("\nThe cat names are:")
    for line in cat_lines:
        print(line.strip())

try:
    with open(dog_filename) as dog_file:
        dog_lines = dog_file.readlines()
except FileNotFoundError:
    '''print(f"File {dog_filename} not found.")'''
    pass
else:
    print("\nThe dog names are:")
    for line in dog_lines:
        print(line.strip())
