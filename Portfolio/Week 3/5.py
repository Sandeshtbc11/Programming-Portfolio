"""
Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time.
"""
# Define the list of common bad passwords
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    # Ask the user to enter a new password
    password1 = input("Enter a new password (8-12 characters): ")

    # Check if the password length is valid
    if len(password1) < 8 or len(password1) > 12:
        print("Error: Password must be between 8 and 12 characters.")
    elif password1 in BAD_PASSWORDS:
        print("Error: BAD PASSWORD")
    else:
        # Prompt the user to re-enter the password
        password2 = input("Re-enter the password: ")

        # Check if the two passwords match
        if password1 == password2:
            print("Password Set")
            break  # Exit the loop if the password is set successfully
        else:
            print("Error: Passwords do not match. Please try again.")
