# 1. Ask for the user's name and write it to name.txt
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2. Read the name from name.txt and greet the user
in_file = open("name.txt", "r")
stored_name = in_file.read().strip()
in_file.close()
print(f"Hi {stored_name}!")

# 3. Read the first two numbers from numbers.txt and print their sum
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    total = first_number + second_number
    print(total)  # should be 59

# 4. Read all numbers from numbers.txt and print their total
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        total += int(line)
    print(total)  # should be 459 for 17+42+400
