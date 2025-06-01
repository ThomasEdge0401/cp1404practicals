"""Convert between Celsius and Fahrenheit using functions."""


# imports
# CONSTANTS


def main():
    """Display menu and process temperature conversions."""
    menu = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"result: {fahrenheit:.2f} f")
        elif choice == "F":
            fahrenheit = float(input("fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"result: {celsius:.2f} c")
        else:
            print("invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("thank you.")


def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return 5 / 9 * (fahrenheit - 32)


main()
