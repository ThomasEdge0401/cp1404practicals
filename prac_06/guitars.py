"""estimate: 20 minutes
actual: 15 minutes

this program manages a collection of guitars.
"""

from guitar import Guitar


def main():
    """manage guitars."""
    guitars = []

    print("my guitars!")
    name = input("name: ")
    while name != "":
        year = int(input("year: "))
        cost = float(input("cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("name: ")

    print("\nthese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
