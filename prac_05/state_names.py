def main():
    code_to_name = {
        "QLD": "Queensland",
        "NSW": "New South Wales",
        "NT": "Northern Territory",
        "WA": "Western Australia",
        "ACT": "Australian Capital Territory",
        "VIC": "Victoria",
        "TAS": "Tasmania",
        "SA": "South Australia"
    }

    print(code_to_name)

    state_code = input("Enter short state: ").upper()
    while state_code != "":
        try:
            print(f"{state_code} is {code_to_name[state_code]}")
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()

    for code in code_to_name:
        print(f"{code:3} is {code_to_name[code]}")


main()
