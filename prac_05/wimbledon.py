FILENAME = "wimbledon.csv"


def main():
    data = read_data(FILENAME)
    champions_to_wins, countries = process_data(data)
    display_champions(champions_to_wins)
    display_countries(countries)


def read_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip header
        return [line.strip().split(",") for line in in_file]


def process_data(data):
    champions_to_wins = {}
    countries = set()
    for row in data:
        champion = row[2]
        country = row[1]
        countries.add(country)
        if champion in champions_to_wins:
            champions_to_wins[champion] += 1
        else:
            champions_to_wins[champion] = 1
    return champions_to_wins, countries


def display_champions(champions_to_wins):
    print("Wimbledon Champions:")
    for name, wins in sorted(champions_to_wins.items()):
        print(f"{name} {wins}")


def display_countries(countries):
    sorted_countries = sorted(countries)
    print(f"\nThese {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))


main()
