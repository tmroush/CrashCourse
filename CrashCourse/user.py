class User:
    """A class to describe a user."""

    def __init__(self, first_name, last_name):
        """Intialize a User with their first and last name."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.full_name = f"{first_name.title()} {last_name.title()}"
        self.login = f"{first_name[0]}{last_name}"
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user information."""
        print(f"{self.full_name}'s login id is {self.login}.")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Good to see you, {self.first_name}.")

    def increment_login_attempts(self):
        """Increment the login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login attempts back to 0."""
        self.login_attempts = 0


class Privileges():

    def __init__(self):
        """Set up the privileges an Admin can do."""
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can add user']

    def show_privileges(self):
        """List out the privileges."""
        print("Admin can do the following:")
        for privilege in self.privileges:
            print(f"\t{privilege.title()}")

class Admin(User):
    def __init__(self, first_name, last_name):
        """Initialize an Admin with their first and last name."""
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


user1 = User('tricia', 'roush')
user1.describe_user()
user1.greet_user()

user2 = User('phil', 'roush')
user2.describe_user()
user2.greet_user()

user3 = User('charles', 'roush')
user3.describe_user()
user3.greet_user()
user3.increment_login_attempts()
user3.increment_login_attempts()
print(f"User3 login attempts: {user3.login_attempts}")
user3.reset_login_attempts()
print(f"User3 login attempts after reset: {user3.login_attempts}")

admin = Admin('big', 'boss')
admin.privileges.show_privileges()
