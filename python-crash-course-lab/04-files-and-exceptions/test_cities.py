import unittest
from city_function import city_country

class CityTestCase(unittest.TestCase):

    def test_first_city(self):
        formatted_city = city_country('Tyumen', 'Russia')
        self.assertEqual(formatted_city, 'Tyumen, Russia')

    def test_last_city(self):
        formatted_city = city_country('Tyumen', 'Russia', '850000')
        self.assertEqual(formatted_city, 'Tyumen, Russia, Population = 850000')

if __name__ == '__main__':
    unittest.main()