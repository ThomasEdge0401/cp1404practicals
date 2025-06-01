"""Password Check with Functions"""


# imports
# CONSTANTS



def main():
    """Get password and display asterisks."""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Prompt user for a valid password (at least 5 characters)."""
    password = input("Enter password: ")
    while len(password) < 5:
        print("Password too short")
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    """Print asterisks equal to password length."""
    print("*" * len(password))


main()
