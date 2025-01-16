"""
When processing data it is oen useful to remove the last character from some
input (it is oen a newline). Write and test a function that takes a string parameter
and returns it with the last character removed. (If the string contains one or fewer
characters, return it unchanged.)
"""
# Function to remove the last character of the string using slicing
def remove_last_char(s):
    return s[:-1] if len(s) > 1 else s

# Test the function
input_string = input("Enter a string: ")
print("Modified string:", remove_last_char(input_string))
