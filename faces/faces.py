# take user input in a function called convert
# convert it to real emojies
# show output
def convert():
    face = input("say something with emoji").replace(":)","🙂").replace(":(","🙁")
    print(face)
def main():
    convert()


main()
