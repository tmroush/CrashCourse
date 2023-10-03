"""10-5: Prompt users to take a poll."""

filename = 'programmer_poll.txt'
with open(filename, 'a') as file_object:
    while True:
        answer = input("Why do you like programming? (Enter 'q' to quit.) ")
        if answer == "q":
            break;
        else:
            line = f"{answer}\n"
            file_object.write(line)
