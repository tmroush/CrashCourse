def describe_city(city, country='united states'):
    """Write a sentence about the city and country"""
    print(f"{city.title()} is in {country.title()}.")

def city_country(city, country):
    """Return the city and country, neatly formatted."""
    return f"{city.title()}, {country.title()}"

describe_city('denver')
describe_city(city = 'rome', country = 'italy')
describe_city('frankfurt', 'germany')

print(city_country('rome', 'italy'))
print(city_country('quito', 'ecuador'))
print(city_country('st. petersburg', 'russia'))
