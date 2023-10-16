import inflect

def bid_adieu(name):
    p = inflect.engine()
    length = len(names)
    if length == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif length == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        farewell = f"Adieu, adieu, to {', '.join(names[:-1])}"
        farewell += f", and {names[-1]}"
        print(farewell)


if __name__ == "__main__":
    names = []
    print("Name: ")
    try:
        while True:
            name = input()
            names.append(name) ## add the names to the name list.
    except EOFError:
        bid_adieu(names)