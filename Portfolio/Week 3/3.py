"""
Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long.
"""
# Ask the user to enter password
password1 = input("Enter a password (8-12 characters): ")

# Check if the password length is valid
if len(password1) < 8 or len(password1) > 12:
    print("Error: Password must be between 8 and 12 characters.")
else:
    # Prompt the user to re-enter the password
    password2 = input("Re-enter the password: ")

    # Check if the two passwords match
    if password1 == password2:
        print("Password Set")
    else:
        print("Error: Passwords do not match. Please try again.")
