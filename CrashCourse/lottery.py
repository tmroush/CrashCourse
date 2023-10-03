from random import choice

possible_values = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e')

choice1 = choice(possible_values)
choice2 = choice(possible_values)
choice3 = choice(possible_values)
choice4 = choice(possible_values)

print(f"The winning ticket must match {choice1} {choice2} {choice3} {choice4}.")

my_ticket = (choice1, choice2, choice3, choice4)
tries = 0

while True:
    match1 = choice(possible_values)
    match2 = choice(possible_values)
    match3 = choice(possible_values)
    match4 = choice(possible_values)
    tries += 1
    if my_ticket[0] == match1 and my_ticket[1] == match2 and my_ticket[2] == match3 and my_ticket[3] == match4:
        break;

print(f"It took {tries} tries to get a matching ticket.")
