num_people = input("How many people are in your party? ")
num_people = int(num_people)

if num_people > 8:
    print("\nYour party will need to wait for a table.")
else:
    print("\nYour party may be seated now.")