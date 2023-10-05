import json


def get_stored_username():
    """Get the stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
       return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    filename = 'username.json'
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()

    if username:
        prompt = f"Is {username} your name? (y/n): "
        correct_username = input(prompt)
        if correct_username == "y":
            print(f"Welcome back, {username}!")
        else:
            print("I'm sorry. Let's fix that.")
            username = get_new_username()
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()
