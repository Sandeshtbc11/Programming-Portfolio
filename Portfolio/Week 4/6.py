"""
Write a program that takes a centigrade temperature and displays the equivalent in
fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format.
"""
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Ask the user to input a temperature in Celsius
input_temp = input("Enter temperature in Celsius (e.g., 25C): ")

# Check if the input ends with 'C' and contains a valid number
if input_temp[-1] == "C" or input_temp[-1] == "c":
    number_part = input_temp[:-1]
    if number_part.replace(".", "", 1).isdigit():
        celsius = float(number_part)
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{fahrenheit}F")
    else:
        print("Invalid input. Please enter a number followed by 'C'.")
else:
    print("Invalid input. Please enter a number followed by 'C'.")

