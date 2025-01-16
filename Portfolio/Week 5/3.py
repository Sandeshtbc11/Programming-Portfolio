"""
Write a program that takes a bunch of command-line arguments, and then prints
out the shortest. If there is more than one of the shortest length, any will do.
Hint: Don't overthink this. A good way to find the shortest is just to sort them
"""
import sys  

# Get all command-line arguments
arg = sys.argv[1:]  

# Find the shortest argument by length
arg_sort = min(arg, key=len)  

# Print the shortest argument
print(f'Shortest argument is: {arg_sort}')  
