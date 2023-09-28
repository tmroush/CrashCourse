# Counting to twenty

for i in range(1, 21):
    print(i)

# Counting to one million
million = list(range(1, 1000001))
# for num in million:
#   print(num)

# min and max to check, and then sum
print(f"Minimum is {min(million)}.")
print(f"Maximum is {max(million)}.")
print(f"Sum is {sum(million)}.")

# list of odd numbers
odds = list(range(1, 20, 2))
print("The odd numbers are: ")
for num in odds:
    print(num)

# list of multiples of 3
mults = list(range(3, 30, 3))
print("The multiples of 3 are: ")
for num in mults:
    print(num)

# cubes
cubes = []
for value in range (1, 11):
    cubes.append(value ** 3)

print("The cubes are: ")
for cube in cubes:
    print(cube)

# Use a list comprehension
cubes_alt = [value**3 for value in range(1, 11)]
print(cubes_alt)
