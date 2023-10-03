from random import randint

class Die:

    def __init__(self, num_sides=6):
        """Initialize a num_sides die"""
        self.num_sides = num_sides

    def roll_die(self):
        roll = randint(1, self.num_sides)
        print(f"You rolled a {roll}!")


die1 = Die()
die1.roll_die()

die10 = Die(10)
die10.roll_die()
