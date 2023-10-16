import random
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass
def generate_an_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("invalid level")

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_an_integer(level)
        y = generate_an_integer(level)
        correc_result = x + y
        attempt = 0

        while attempt < 3:
            try:
                question = int(input(f"{x} + {y} ="))
                if question == correc_result:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempt += 1
                    if attempt == 3:
                        print(f"{x} + {y} ={correc_result}")

            except ValueError:
                print("EEE")
                attempt += 1
    print(f"Score: {score}")

if __name__== "__main__":
    main()