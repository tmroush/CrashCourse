prompt = "I will tell you if a number is a multiple of 10."
prompt += "\nPlease enter a number: "

number = input(prompt)
number = int(number)
if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of 10!")
else:
    print(f"\nThe number {number} is NOT a multiple of 10!")
