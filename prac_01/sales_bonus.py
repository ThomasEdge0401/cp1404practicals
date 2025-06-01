sales = float(input("enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    elif sales >= 1000:
        bonus = sales * 0.15
    print(f"bonus: ${bonus:.2f}")
    sales = float(input("enter sales: $"))
