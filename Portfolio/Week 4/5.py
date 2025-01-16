""""
Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae).
"""
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Test the functions
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equivalent to {fahrenheit}°F")

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
celsius_result = fahrenheit_to_celsius(fahrenheit_input)
print(f"{fahrenheit_input}°F is equivalent to {celsius_result}°C")
