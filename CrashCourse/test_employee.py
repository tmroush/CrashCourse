import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test the Employee give_raise() method."""
    def setUp(self):
        self.employee = Employee('Tricia', 'Roush', 100000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 105000)  # add assertion here

    def test_give_custom_raise(self):
        self.employee.give_raise(3000)
        self.assertEqual(self.employee.salary, 103000)


if __name__ == '__main__':
    unittest.main()
