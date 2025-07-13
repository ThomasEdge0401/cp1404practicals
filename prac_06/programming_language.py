"""estimate: 20 minutes
actual: 15 minutes

this module defines the programminglanguage class.
"""


class ProgrammingLanguage:
    """represent a programming language object."""

    def __init__(self, name, typing, reflection, year):
        """initialise a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """return true if typing is dynamic."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """return string representation of programming language."""
        return f"{self.name}, {self.typing} typing, reflection={self.reflection}, first appeared in {self.year}"
