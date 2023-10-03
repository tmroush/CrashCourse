from car import Car


class Battery:
    """A simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery."""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def upgrade_battery(self):
        """Upgrade the battery to 100kwh, but only if it us a 75kwh battery."""
        if self.battery_size != 100:
            self.battery_size = 100;

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size -- 100:
            range = 315

        print(f'This car can go about {range} miles on a full charge.')


class ElectricCar(Car):
    """Represents an Electric Car."""

    def __init__(self, make, model, year):
        """Initialize attributes of parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gass tanks."""
        print("Electric cars don't have gas tanks.")
