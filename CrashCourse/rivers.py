# a dictionary of rivers and their countries. The key is the river
rivers = {
    'nile': 'egypt',
    'danube': 'germany',
    'mississippi': 'united states',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nAll the rivers are:")

for river in rivers.keys():
    print(river.title())

print("\nAll the countries are:")

for country in rivers.values():
    print(country.title())
