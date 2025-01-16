"""
Write a program that, when run from the command line, reports how many
arguments were provided. (Remember that the program name itself is not an
argument).
"""
import sys

# Calculate the number of command-line arguments
num_arguments = len(sys.argv) - 1

# Report the result
print(f"Number of arguments provided: {num_arguments}")
