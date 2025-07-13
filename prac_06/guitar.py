"""estimate: 20 minutes
actual: 15 minutes

this module defines the guitar class.
"""


class Guitar:
    """represent a guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """initialise a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """return string representation of guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """return the age of the guitar in years."""
        current_year = 2025
        return current_year - self.year

    def is_vintage(self):
        """return true if guitar is 50 or more years old."""
        return self.get_age() >= 50
