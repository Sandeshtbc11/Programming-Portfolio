"""
Last week you wrote a program that processed a collection of temperature readings
entered by the user and displayed the maximum, minimum, and mean. Create a
version of that program that takes the values from the command-line instead. Be
sure to handle the case where no arguments are provided!
"""
import sys 

# Check if there are any command-line arguments
if len(sys.argv) > 1:
    try:
        # Convert each command-line argument
        temperatures = [float(arg) for arg in sys.argv[1:]]

        # Calculate the maximum, minimum, and mean temp.
        maximum = max(temperatures)
        minimum = min(temperatures)
        mean = sum(temperatures) / len(temperatures)

        # Display the results
        print(f"Maximum temperature: {maximum}")
        print(f"Minimum temperature: {minimum}")
        print(f"Mean temperature: {mean}")
    except ValueError:
        print("Please provide valid numeric temperature readings.")
else:
    print("No temperature readings provided.")
