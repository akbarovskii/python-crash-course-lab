class Employee:
    """Модель работника с возможностью повышения оклада."""

    def __init__(self, first_name, last_name, annual_salary):
        """Сохраняет имя, фамилию и ежегодный отклад."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount = 5000):
        """Увеличивет оклад на заданную сумму (по умолчанию на 5000)."""
        self.annual_salary += amount