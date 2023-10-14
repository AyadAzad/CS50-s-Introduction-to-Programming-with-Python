import emoji

def emojize_text(user_input):
   return emoji.emojize(user_input, language='alias')

def main():
    userInput = input("Input :")
    outPut = emojize_text(userInput)
    print("Output: ", outPut)


if __name__ == "__main__":

    main()

