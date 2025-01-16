"""
Modify the previous program so that it can process any number of values. The input
terminates when the user just pressed "Enter" at the prompt rather than entering a
value.
"""
# Initialize an empty list to store the temperatures
temperatures = []

# Ask the user to enter temperatures
while True:
    # Ask for the temperature input
    temp = input("Enter a temperature (or press Enter to finish): ")
    
    # Break the loop 
    if temp == "":
        break
    
    # Convert the input to a float and add it to the list
    temperatures.append(float(temp))

# Check if there are any temperatures entered
if temperatures:
    # Calculate the maximum, minimum, and mean
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)

    # Display the results
    print(f"Maximum temperature: {max_temp}")
    print(f"Minimum temperature: {min_temp}")
    print(f"Mean temperature: {mean_temp}")
else:
    print("No temperatures were entered.")
