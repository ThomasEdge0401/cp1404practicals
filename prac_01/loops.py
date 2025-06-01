# part a
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# part b
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# part c
for i in range(20, 0, -1):
    print(i, end=' ')
print()

number = int(input("number of stars: "))
for i in range(number):
    print("*", end='')
print()

# part d
for i in range(1, number + 1):
    print("*" * i)
