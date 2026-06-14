# This program greets you and calculates years until you turn 100
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Calculate years remaining
years_left = 100 - age

# Display the result
print(f"Hello, {name}!")
print(f"You will turn 100 years old in {years_left} years.")
