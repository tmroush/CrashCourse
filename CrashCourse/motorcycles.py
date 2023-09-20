# Learning about lists.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Appending to a list
motorcycles.append('ducati')
print("Appended ducati:")
print(motorcycles)

# Inserting into a list at a specific position
motorcycles.insert(2, 'harley davidson')
print("Inserted harley davidson at 2: ")
print(motorcycles)

# Deleting an item from a list
del motorcycles[1]
print("Deleted [1] from the list:")
print(motorcycles)

# If you want to use an item as you delete it, use pop()
popped_motorcycle = motorcycles.pop()
print("Popped motorcycle: " + popped_motorcycle)
print(motorcycles)

# add the popped item back so we have more items to work with.
motorcycles.append(popped_motorcycle)
print("Added popped motorcycle back:")
print(motorcycles)

# You can pop from anywhere in the list by passing the index:
first_motorcylce = motorcycles.pop(0)
print(f"The first motorcycle in the list was {first_motorcylce.title()}.")

# You can also remove by value
motorcycles.append(first_motorcylce)
motorcycle = 'suzuki'
motorcycles.remove(motorcycle)
print(f"Removed {motorcycle} from the list, because who would want one?")
print(motorcycles)


