print('This program can add two numbers.')
print('(Enter "q" to quit.')

while True:
    number_1 = input("Enter the first number to add: ")
    if number_1 == "q":
        break

    number_2 = input("Enter the second number: ")
    if number_2 == "q":
        break

    try:
        value_1 = int(number_1)
        value_2 = int(number_2)
    except ValueError:
        ''' print("You didn't input numbers!") '''
        pass
    else:
        answer = value_1 + value_2
        print(f"The answer is {answer}.")
