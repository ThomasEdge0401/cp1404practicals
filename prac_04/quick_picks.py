import random

MIN = 1
MAX = 45
NUMBERS_PER_LINE = 6


def main():
    quick_picks = int(input("How many quick picks? "))
    for _ in range(quick_picks):
        line = []
        while len(line) < NUMBERS_PER_LINE:
            number = random.randint(MIN, MAX)
            if number not in line:
                line.append(number)
        line.sort()
        print(" ".join(f"{n:2}" for n in line))


main()
