squares = []
for value in range (1, 11):
    squares.append(value ** 2)

print(squares)

print(f"Minimum of squares is {min(squares)}")
print(f"Maximum of squares is {max(squares)}")
print(f"Sum of squares is {sum(squares)}")

# alternative way to create the squares list:
squares_alt = [value**2 for value in range(1, 11)]
print(squares_alt)

