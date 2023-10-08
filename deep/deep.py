user = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
user = user.strip().lower()
if user == "42" or user=="forty-two" or user == "forty two":
    print("Yes")
else:
    print("No")