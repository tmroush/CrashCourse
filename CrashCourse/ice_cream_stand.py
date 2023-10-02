from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """The IceCreamStand is a specific type of Restaurant."""

    def __init__(self, stand_name):
        """
        Initialize the attributes of the parent class.
        Then initialize things we need for this class
        :param stand_name: the name of the Ice Cream Stand
        """
        super().__init__(stand_name, "dessert")
        self.flavors = ['vanilla', 'chocolate', 'rocky road', 'neopolitan']

    def display_flavors(self):
        """Display the list of flavors at this Ice Cream stand."""
        print(f"\nThe ice cream flavors at {self.name} are:")
        for flavor in self.flavors:
            print(f"\t{flavor.title()}")

    def add_flavor(self, new_flavor):
        """Add the new flavor"""
        self.flavors.append(new_flavor)


ice_cream_stand = IceCreamStand('cold stone creamery')
ice_cream_stand.display_flavors()

