
menu = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(menu)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"result: {fahrenheit:.2f} f")
    elif choice == "F":
        fahrenheit = float(input("fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"result: {celsius:.2f} c")
    else:
        print("invalid option")
    print(menu)
    choice = input(">>> ").upper()
print("thank you.")
