"""Menu-based score program with validation, evaluation, and star display."""


# imports
# CONSTANTS


def main():
    """Run the score menu program."""
    score = get_valid_score()
    choice = display_menu()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(evaluate_score(score))
        elif choice == "S":
            print("*" * int(score))
        else:
            print("invalid option")
        choice = display_menu()
    print("goodbye")


def display_menu():
    """Display the menu and get user's choice."""
    print("\n(G)et score\n(P)rint result\n(S)how stars\n(Q)uit")
    return input(">>> ").upper()


def get_valid_score():
    """Prompt user for a valid score between 0 and 100 inclusive."""
    score = float(input("enter score: "))
    while score < 0 or score > 100:
        print("invalid score")
        score = float(input("enter score: "))
    return score


def evaluate_score(score):
    """Return the result based on the score value."""
    if score >= 90:
        return "excellent"
    elif score >= 50:
        return "passable"
    else:
        return "bad"


main()
