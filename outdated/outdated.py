from datetime import datetime
# using datetime package.
# learn more about date in python
this_list = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        userInput = input("Date: ").strip()
        # Check if the input is enclosed in double quotes
        if userInput.startswith('"') and userInput.endswith('"'):
            userInput = userInput[1:-1].strip()

        userinput = userInput.title()
        # checking user's input to reverse it
        if "/" in userInput:
            date = datetime.strptime(userInput, "%m/%d/%Y")
            iso_date = date.strftime("%Y-%m-%d")
            print(iso_date)
            break
        else:
            # Split the input into parts
            parts = userInput.split()

            # Check if the first part is a valid month name
            # then change it to number using date.strftime
            if parts[0] in this_list:
                month_number = this_list.index(parts[0]) + 1
                day = int(parts[1][:-1])
                year = int(parts[2])

                date = datetime(year, month_number, day)

                iso_date = date.strftime("%Y-%m-%d")
                print(iso_date)
                break
    except ValueError:
        pass
