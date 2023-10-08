accepted_values = [5, 10, 25]
inserted_value = 0

while inserted_value < 50:
    coin = int(input("Insert a coin: "))
    if coin in accepted_values:
        inserted_value = inserted_value + coin
        if inserted_value < 50:
             print(f"Amount Due: {50 - inserted_value}")
    else:
        print("Amount Due: 50")
        break
    if inserted_value >= 50:
        break

change = inserted_value - 50
if change > 0:
    print(f"Change Owed: {change}")
elif change == 0:
    print("Change Owed: 0")


