"""
Write a program that reads 6 temperatures (in the same format as before), and
displays the maximum, minimum, and mean of the values.
Hint: You should know there are built-in functions for max and min. If you hunt, you
might also find one for the mean.
"""
# Ask the user for 6 temperatures
temp1 = float(input("Enter temperature 1: "))
temp2 = float(input("Enter temperature 2: "))
temp3 = float(input("Enter temperature 3: "))
temp4 = float(input("Enter temperature 4: "))
temp5 = float(input("Enter temperature 5: "))
temp6 = float(input("Enter temperature 6: "))

# Store the temperatures in a list
temperatures = [temp1, temp2, temp3, temp4, temp5, temp6]

# Calculate the maximum, minimum, and mean
max_temp = max(temperatures)
min_temp = min(temperatures)
mean_temp = sum(temperatures) / len(temperatures)

# Display the results
print(f"Maximum temperature: {max_temp}")
print(f"Minimum temperature: {min_temp}")
print(f"Mean temperature: {mean_temp}")
