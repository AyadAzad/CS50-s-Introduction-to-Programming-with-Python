
def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False

    if not s.isalnum():
        return False

    if s.endswith("0"):
        return True

    if '0' in s:
        return False

    if s[1:].isdigit():
        return False

    return True


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

main()