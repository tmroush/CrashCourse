def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


def print_profile(user_info):
    """Neatly print out the contents of user_info"""
    print("\nThe user_info contains: ")
    for key, value in user_info.items():
        print(f"user_info[{key}] = {value}.")
