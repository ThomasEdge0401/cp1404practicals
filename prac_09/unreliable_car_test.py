from unreliable_car import UnreliableCar

def main():
    car1 = UnreliableCar("Mostly Reliable", 100, 90)
    car2 = UnreliableCar("Dodgy", 100, 30)

    print("driving Mostly Reliable car 10 times")
    for i in range(10):
        distance = car1.drive(10)
        print(f"attempt {i + 1}: drove {distance} km | fuel left: {car1.fuel}")

    print("\ndriving Dodgy car 10 times")
    for i in range(10):
        distance = car2.drive(10)
        print(f"attempt {i + 1}: drove {distance} km | fuel left: {car2.fuel}")

main()
