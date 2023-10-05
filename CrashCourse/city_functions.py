
def format_city_country(city, country, population=''):
    """Format the city and country into a string City, Country"""
    if population:
        formatted_name = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_name = f"{city.title()}, {country.title()}"
    return formatted_name
