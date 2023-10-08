user = input("Expression :")
x, operator, z = user.split()

x = int(x)
z = int(z)

result = 0.0

if operator == '+':
    result = x + z
elif operator == '-':
    result = x - z
elif operator == '*':
    result = x * z
elif operator == '/':
    if z != 0:
        result = x / z
    else:
        print("Error: Division by zero is not allowed.")
        exit(1)
else:
    print("Error: Invalid operator. Please use +, -, *, or /.")
    exit(1)


formattedResult = "{:.1f}".format(result)
print(formattedResult)
