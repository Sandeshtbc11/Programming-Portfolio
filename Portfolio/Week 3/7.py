"""
Modify your "Times Table" program so that the user enters the number of the table
they require. This number should be between 0 and 12 inclusive.
"""
# Ask the user for a number between 0 and 12
number = int(input("Enter a number between 0 and 12 to see its times table: "))

# Check if the number is within the valid range
if 0 <= number <= 12:
    # Displaying the table for the entered number
    for i in range(13):
        print(f"{i} x {number} = {i * number}")
else:
    print("Error: Please enter a number between 0 and 12.")
