"""
Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program.
"""
# Function to count uppercase and lowercase 
def count_case(s):
    uppercase_count = 0
    lowercase_count = 0
    
    for char in s:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    
    return uppercase_count, lowercase_count

# Test the function
input_string = input("Enter a string: ")
uppercase, lowercase = count_case(input_string)

print(f"Uppercase letters: {uppercase}")
print(f"Lowercase letters: {lowercase}")