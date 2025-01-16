"""
Modify your program again so that the chosen password cannot be one of a list of
common passwords, defined thus:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
"""
# Define the list of common bad passwords
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

# Ask the user to enter a new password
password1 = input("Enter a new password (8-12 characters): ")

# Check if the password length is valid
if len(password1) < 8 or len(password1) > 12:
    print("Error: Password must be between 8 and 12 characters.")
elif password1 in BAD_PASSWORDS:
    print("Error: BAD PASSWORD")
else:
    # Ask the user to re-enter the password
    password2 = input("Re-enter the password: ")

    # Check if the two passwords match
    if password1 == password2:
        print("Password Set")
    else:
        print("Error: Passwords do not match. Please try again.")
