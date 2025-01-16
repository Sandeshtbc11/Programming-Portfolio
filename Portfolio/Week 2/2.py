"""
Write a program that prompts a user to enter a temperature in Celsius, and then
displays the corresponding temperature in Fahrenheit, like so:
Enter a temperature in Celsius: 32.5
32.5C is equivalent to 90.5F.
"""
# Ask the user to enter a temperature in Celsius
celsius = float(input("Enter a temperature in Celsius: "))

# Converting Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Displaying the result
print(f"{celsius} C is equivalent to {fahrenheit} F.")