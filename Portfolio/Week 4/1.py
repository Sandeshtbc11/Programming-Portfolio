"""
Functions are oen used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise. Write a short program to test the function.
"""
# Function to check if the number is in the range 0 to 100
def is_valid_number(number):
    return 0 <= number <= 100

# Test the function
number = int(input("Enter a number: "))
if is_valid_number(number):
    print(f"{number} is in the valid range (0 to 100).")
else:
    print(f"{number} is out of the valid range (0 to 100).")
