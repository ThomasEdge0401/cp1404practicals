from guitar import Guitar


def main():
    guitars = load_guitars("guitars.csv")
    print("These are my guitars:")
    display_guitars(guitars)

    guitars.sort()  # uses __lt__ in Guitar

    print("\nThese are my guitars sorted by year:")
    display_guitars(guitars)

    guitars += add_new_guitars()
    save_guitars("guitars.csv", guitars)


def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def add_new_guitars():
    guitars = []
    print("\nAdd new guitars (leave name blank to finish):")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")
    return guitars


def save_guitars(filename, guitars):
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
