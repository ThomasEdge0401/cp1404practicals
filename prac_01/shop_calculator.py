number_of_items = int(input("number of items: "))
while number_of_items < 0:
    print("invalid number of items!")
    number_of_items = int(input("number of items: "))

total_price = 0
for i in range(number_of_items):
    price = float(input("price of item: "))
    total_price += price

if total_price > 100:
    total_price *= 0.9

print(f"total price for {number_of_items} items is ${total_price:.2f}")
