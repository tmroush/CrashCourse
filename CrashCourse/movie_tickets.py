prompt = "\nPlease enter your age so we can calculate the price of your ticket: "
prompt += "\nEnter 'quit' when you are done. "

age = ""
total = 0

while age != 'quit':
    age = input(prompt)

    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("\nYour ticket is free!")
    elif 3 <= age <= 12:
        print("\nYour ticket is $10.")
        total += 10
    else:
        print("\nYour ticket is $15.")
        total += 15

print(f"The total for your tickets will be ${total}.")
