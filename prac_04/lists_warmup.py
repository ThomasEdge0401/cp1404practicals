def main():
    numbers = [3, 1, 4, 1, 5, 9, 2]

    # Predicted values (before testing):
    # numbers[0] → 3
    # numbers[-1] → 2
    # numbers[3] → 1
    # numbers[:-1] → [3, 1, 4, 1, 5, 9]
    # numbers[3:4] → [1]
    # 5 in numbers → True
    # 7 in numbers → False
    # "3" in numbers → False
    # numbers + [6, 5, 3] → [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

    # List manipulation:
    numbers[0] = "ten"
    numbers[-1] = 1
    print(numbers[2:])  # Print all except the first two
    print(9 in numbers)  # Check if 9 is in the list

main()
