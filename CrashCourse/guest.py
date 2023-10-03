"""10-3: Write a program that prompts the user for thier name."""
"""When they respond, write their name to a file called guest.txt."""

filename = 'guest.txt'

name = input("Please enter your name: ")

with open(filename, 'w') as file_object:
    file_object.write(name)
