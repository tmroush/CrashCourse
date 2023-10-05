import unittest
from city_functions import format_city_country

class CitiesCountriesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """Do names like santiago and chile work?"""
        formatted_name = format_city_country("santiago", "chile")
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_county_population(self):
        """Do names like santiago, chile, population=5000000"""
        formatted_name = format_city_country('santiago', 'chile', population='5000000')
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()
