def convert(text):
    vowls = "AEIOUaeiou"
    withoutvowls = ''.join(char for char in text if char not in vowls)
    return withoutvowls


def main():
    userinput = input("Input")
    useroutput = convert(userinput)
    print("Output : ", useroutput)

if __name__ == "__main__":
    main()

