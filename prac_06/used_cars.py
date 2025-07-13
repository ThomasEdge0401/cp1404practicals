from car import Car


def main():
    """demo test code to show how to use car class."""
    my_car = Car("my car", 180)
    my_car.drive(30)
    print(f"car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car("limo", 100)
    limo.add_fuel(20)
    print(f"limo has fuel: {limo.fuel}")
    limo.drive(115)
    print(limo)


main()
