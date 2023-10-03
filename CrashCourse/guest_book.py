"""10-4: Prompt users to fill in a guestbook."""

filename = 'guest_book.txt'
with open(filename, 'a') as file_object:
    while True:
        name = input("Please enter your name, or 'q' to quit: ")
        if name == "q":
            break;
        else:
            line = f"{name}\n"
            file_object.write(line)

