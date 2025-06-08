import random

# line 1: generates a random integer between 5 and 20, inclusive
print(random.randint(5, 20))  # smallest: 5, largest: 20

# line 2: generates a random odd number between 3 and 9 (step of 2)
print(random.randrange(3, 10, 2))  # smallest: 3, largest: 9, could be: 3, 5, 7, 9 (not 4)

# line 3: generates a random float between 2.5 and 5.5
print(random.uniform(2.5, 5.5))  # smallest: 2.5, largest: 5.5

# random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(random_number)
