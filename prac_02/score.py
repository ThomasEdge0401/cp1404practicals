"""Get score from user, evaluate it, and print result."""


# imports
import random
# CONSTANTS


def main():
    """Get user's score and print result, then show random score result."""
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(result)

    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score:.2f}")
    print(evaluate_score(random_score))


def evaluate_score(score):
    """Return the result based on the score value."""
    if score < 0 or score > 100:
        return "invalid score"
    elif score >= 90:
        return "excellent"
    elif score >= 50:
        return "passable"
    else:
        return "bad"


main()
