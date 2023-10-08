M = int(input("m: "))  # Prompt the user for mass in kilograms
E = 300000000  # Speed of light in meters per second
result = M * E**2
rounded_result = round(result)  # Round the result to the nearest integer
print("E: ", rounded_result)