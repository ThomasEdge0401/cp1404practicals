is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # finish only if input is valid
    except ValueError:  # only catch ValueError, not all exceptions
        print("Please enter a valid integer.")
print("Valid result is:", result)
