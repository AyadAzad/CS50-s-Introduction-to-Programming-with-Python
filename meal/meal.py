def main():
    time_str = input("Enter the time :")
    time = convert(time_str)

    if  7<= time <= 8:
        print("breakfast time")

    elif  12<= time <= 13:
        print("lunch time")

    elif  18<= time <= 19:
        print("dinner time")

def convert(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return hours + minutes / 60.0


if __name__ == "__main__":
    main()