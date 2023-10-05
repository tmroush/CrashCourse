class Employee():
    """A representation of an Employee."""

    def __init__(self, firstname, lastname, salary):
        """Create an Employee with the firstname, lastname, and annual salary given."""
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def give_raise(self,salary_increase=5000):
        """Give the person a raise by salary_increase. If no amount is specified, it defaults to $5000."""
        self.salary += salary_increase

