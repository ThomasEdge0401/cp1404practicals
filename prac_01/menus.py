name = input("enter name: ")
menu = "(H)ello\n(G)oodbye\n(Q)uit"
print(menu)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"hello {name}")
    elif choice == "G":
        print(f"goodbye {name}")
    else:
        print("invalid choice")
    print(menu)
    choice = input(">>> ").upper()
print("finished.")
