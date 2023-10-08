grocery = {}
try :
    while True :
        userInput = input()
        userInput = userInput.lower()

        if not userInput:  # If the user presses Enter without input, exit the loop
            break

        if userInput in grocery:
             grocery[userInput] += 1
        else:
            grocery[userInput] = 1

except EOFError:
    pass

sorted_items = sorted(grocery.items(), key=lambda x: x[0])
for item, count in sorted_items:
    print(f"{count} {item.upper()}")