# Exercise 3-8 from Python Crash Course
locations = ['rome', 'pyramids', 'quito', 'alaska', 'galapagos islands', 'japan']
print('The original locations list:')
print(locations)

print('\nTemporarily sorted locations list:')
print(sorted(locations))

print('The original locations list:')
print(locations)

print('\nTemporarily sorting in reverse alpahbetical order:')
print(sorted(locations, reverse=True))

print('The original locations list:')
print(locations)

locations.reverse()
print('\nCalled locations.reverse(): ')
print(locations)

locations.reverse()
print('\nCalled locations.reverse() again to put it back: ')
print(locations)

locations.sort()
print('\nCalled locations.sort() to permanently sort the list: ')
print(locations)

locations.sort(reverse=True)
print('\nCalled locations.sort(reverse=True) to permanently reverse sort the list: ')
print(locations)

# From exercise 3-9, instead of editing guest_list, I thought I would do it here
print(f"The length of locations is: {len(locations)}.")
