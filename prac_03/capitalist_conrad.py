import random

def main():
    maximum_increase = 0.175  # 17.5%
    maximum_decrease = 0.05
    minimum_price = 1.0
    maximum_price = 100.0
    starting_price = 10.0
    filename = "output.txt"

    price = starting_price
    number_of_days = 0

    out_file = open(filename, "w")
    print(f"Starting price: ${price:,.2f}", file=out_file)

    while price >= minimum_price and price <= maximum_price:
        number_of_days += 1
        if random.randint(1, 2) == 1:
            price_change = random.uniform(0, maximum_increase)
        else:
            price_change = random.uniform(-maximum_decrease, 0)

        price *= 1 + price_change
        print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

    out_file.close()

main()
