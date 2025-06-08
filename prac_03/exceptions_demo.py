"""
Answer the following questions:
1. When will a ValueError occur?
   - When the user enters something that is not an integer (e.g., a letter or blank input).

2. When will a ZeroDivisionError occur?
   - When the user enters 0 as the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   - Yes, use a loop to prompt again if the denominator is 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
