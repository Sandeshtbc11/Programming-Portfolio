"""
A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
first count the sweets and then divide them according to how many pupils attend
that day. Write a program that will tell the teacher how many sweets to give to each
pupil, and how many she will have le over.
"""
# Asking the user for the number of sweets and the number of pupils
sweets = int(input("How many sweets are there? "))
pupils = int(input("How many pupils are there? "))

# Calculating the number of sweets per pupil and leftover sweets
sweets_per_pupil = sweets // pupils
leftover_sweets = sweets % pupils

# Displaying the result
print(f"Each pupil will get {sweets_per_pupil} sweets.")
print(f"There will be {leftover_sweets} sweets left over.")
