import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """Create an employee instance for all test methods."""
        self.my_employee = Employee('Иван', 'Петров', 50000)

    def test_give_default_raise(self):
        """Test that a default raise increases the salary by 5000."""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 55000)

    def test_give_custom_raise(self):
        """Test that a custom raise increases the salary by a specific amount."""
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.annual_salary, 60000)

if __name__ == '__main__':
    unittest.main()
