"""estimate: 10 minutes
actual: 5 minutes

this module tests the guitar class.
"""

from guitar import Guitar


def main():
    """test the guitar class."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 500)

    print(f"{gibson.name} get_age() - expected 103. got {gibson.get_age()}")
    print(f"{another.name} get_age() - expected 12. got {another.get_age()}")
    print(f"{gibson.name} is_vintage() - expected true. got {gibson.is_vintage()}")
    print(f"{another.name} is_vintage() - expected false. got {another.is_vintage()}")


main()
