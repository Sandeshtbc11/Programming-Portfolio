"""
Write a function that accepts a positive integer as a parameter and then returns a
representation of that number in binary (base 2).
Hint: This is in many ways a trick question. Think!
"""
def binary(num):
    # Check if the input number is positive
    if num > 0:
        # Convert the number to binary using bin()
        return bin(num)[2:]
    else:
        # Print an error message if not positive
        print("Enter positive value")

#Convert the number 10 to its binary representation
print(binary(10))
