prompt = "\nPlease enter a pizza topping (enter 'quit' to stop adding pizza toppings): "

getToppings = True

while getToppings:
    topping = input(prompt)
    if topping == 'quit':
        getToppings = False
    else:
        print(f"We will add {topping} to your pizza.")
