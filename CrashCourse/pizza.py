pizza_types = ['hawaiian', 'pepperoni', 'cheese', 'meat', 'spinach & mushroom']
for pizza in pizza_types:
    print(f"Some people like to eat {pizza.title()} pizza.")

print("\nI like pizza and ate a lot in college.")

# lets add a dictionary with a list example.
pizza_01 = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# summarize the order:
print(f"\nYou ordered a {pizza_01['crust']} - crust pizza "
      "with the following toppings:")
for topping in pizza_01['toppings']:
    print(f"\t{topping}")

