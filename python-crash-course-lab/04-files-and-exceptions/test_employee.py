import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Тесты для класса Employee."""

    def setUp(self):
        """Создает экземпляр работника для всех тестовых методов."""
        self.my_employee = Employee('Иван', 'Петров', 50000)

    def test_give_default_raise(self):
        """Проверяет, что оклад по умолчанию увеличивается на 5000."""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 55000)

    def test_give_custom_raise(self):
        """Проверяет увеличение оклада на произвольную сумму."""
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.annual_salary, 60000)

if __name__ == '__main__':
    unittest.main()
