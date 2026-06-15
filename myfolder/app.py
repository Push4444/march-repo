# Take a integer input from the user
number = int(input("Enter a number to check: "))

# Check if the remainder is 0 when divided by 2
if number % 2 == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")
