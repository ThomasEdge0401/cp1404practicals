from silver_service_taxi import SilverServiceTaxi

def main():
    hummer = SilverServiceTaxi("Hummer", 200, 2)
    hummer.drive(18)
    fare = hummer.get_fare()

    print(hummer)
    print(f"fare: ${fare:.2f}")

    assert round(fare, 2) == 48.80, f"expected $48.80 but got ${fare:.2f}"

main()
