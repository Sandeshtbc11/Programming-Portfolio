"""
Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name dierently. So if the user entered arthur, ARTHUR, or even
arTHur the name should be displayed as Arthur.
"""
# Ask the user to enter their name
name = input("What is your name? ")

# Check if the name is not empty
if name:
    # Format the name with the first letter uppercase and the rest lowercase
    formatted_name = name[0].upper() + name[1:].lower()
else:
    formatted_name = "Stranger"

# Display the greeting
print("Hello, " + formatted_name + ". Good to meet you!")
