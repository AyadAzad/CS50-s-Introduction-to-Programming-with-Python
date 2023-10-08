user = input("pleae enter file name :")
user = user.strip().lower()

if user.endswith(".gif"):
    print("image/gif")

elif user.endswith(".jpg"):
    print("image/jpeg")

elif user.endswith(".jpeg"):
    print("image/jpeg")

elif user.endswith(".png"):
    print("image/png")

elif user.endswith(".pdf"):
    print("application/pdf")

elif user.endswith(".zip"):
    print("application/zip")

elif user.endswith(".txt"):
    print("text/plain")
else :
    print("application/octet-stream")