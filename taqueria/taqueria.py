menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total_cost = 0.00
item_count = 0
while item_count < 3 :
        try :
            userInput = input("Item :")
            userInput = userInput.title()

            if userInput in menu:
                count = menu[userInput]
                total_cost += count
                item_count += 1
                print(f"Total: ${total_cost:.2f}")

        except EOFError:
            break