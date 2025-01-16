"""
Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards. So entering "-7"
would produce the Seven Times Table starting at "12 times" down to "0 times".
"""
# Ask the user for a number between -12 and 12
number = int(input("Enter a number between -12 and 12 to see its times table: "))

# Check if the number is valid
if -12 <= number <= 12:
    # If the number is negative, print the table in reverse order
    if number < 0:
        for i in range(12, -1, -1):  # Loop from 12 to 0
            print(f"{i} x {number * -1} = {i * (number * -1)}")
    else:
        # Displaying the times table for the entered number
        for i in range(13):
            print(f"{i} x {number} = {i * number}")
else:
    print("Error: Please enter a number between -12 and 12.")
