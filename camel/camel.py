def camel_to_snake(camel):
    snake_case = ''
    for char in camel:
        if char.isupper():
            snake_case += '_'+ char.lower()
        else:
            snake_case += char.lower()
    if snake_case.startswith("_"):
        snake_case = snake_case[1:]
    return snake_case


def main():
    camelcase = input("enter a camel case text :")
    snakecase = camel_to_snake(camelcase)
    print("this is the snake case ==>"+ snakecase)


if __name__ == "__main__":
    main()