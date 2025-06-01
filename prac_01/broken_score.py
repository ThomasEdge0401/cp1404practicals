score = float(input("enter score: "))
if score < 0 or score > 100:
    print("invalid score")
elif score >= 90:
    print("excellent")
elif score >= 50:
    print("passable")
else:
    print("bad")
