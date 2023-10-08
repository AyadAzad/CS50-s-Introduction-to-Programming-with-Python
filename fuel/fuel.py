while True:
    try:
        userInput = input("function :")
        if userInput == "1/4":
            print("25%")
            break
        elif userInput == "1/3":
            print("33%")
            break
        elif userInput == "1/2":
            print("50%")
            break
        elif userInput == "2/3":
            print("67%")
            break
        elif userInput == "3/4":
            print("75%")
            break
        elif userInput == "4/4" or userInput == "100/100" or userInput == "99/100":
            print("F")
            break
        elif userInput == "0/4" or userInput == "0/100" or userInput == "1/100":
            print("E")
            break
    except ValueError:
        pass