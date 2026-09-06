class Employee:
    """A model of an employee with the ability to give a salary raise."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize attributes to store first name, last name, and annual salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Increase the annual salary by a given amount (default is 5000)."""
        self.annual_salary += amount
