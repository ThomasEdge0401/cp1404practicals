def main():
    # first output using f-string
    guitar = "Gibson L-5 CES"
    year = 1922
    cost = 16036.0
    print(f"{year} {guitar} for about ${cost:,.0f}!")

    # second output using a loop with string formatting
    for exponent in range(11):
        result = 2 ** exponent
        print(f"2 ^ {exponent:2} is {result:4}")

main()
