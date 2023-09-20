cars = ['bmw', 'audi', 'toyota', 'subaru']
print("List before sorting:")
print(cars)

cars.sort()
print("List after sorting:")
print(cars)

cars.sort(reverse=True)
print("List after reverse sorting:")
print(cars)

cars_2 = ['mcqueen', 'sally', 'mater', 'doc', 'mario', 'fred']
print("\ncars_2: ")
print(cars_2)

temp = sorted(cars_2)
print("\nTesting to see if sorted() returns a sorted list")
print(temp)

cars_2.reverse()
print("\nReversing our cars_2 list: ")
print(cars_2)

length = len(cars_2)
print(f"\nThe number of cars in cars_2 is {length}.")

