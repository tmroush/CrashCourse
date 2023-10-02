class Restaurant:
    """Model of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant."""
        print(f"{self.name.title()} is a {self.cuisine_type.title()} restaurant.")

    def open_restaurant(self):
        """Simulate opening the restaurant."""
        print(f"{self.name.title()} is now open for the day.")

    def set_number_served(self, number_served):
        """Set the number served to the value passed in."""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """Increment the number of people served by the number indicated."""
        self.number_served += number_served


restaurant = Restaurant("casa vallarta", "mexican")
print(f"Number served: {restaurant.number_served}")
restaurant.number_served = 12
print(f"Number served: {restaurant.number_served}")
restaurant.set_number_served(24)
print(f"Number served: {restaurant.number_served}")
restaurant.increment_number_served(120)
print(f"Number served: {restaurant.number_served}")
