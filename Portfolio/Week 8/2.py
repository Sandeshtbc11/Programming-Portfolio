"""
The Unix diff command compares two files and reports the dierences, if any.
Write a simple implementation of this that takes two file names as command-line
arguments and reports whether or not the two files are the same. (Define "same" as
having the same contents.)
"""
file_1_path = "E:/bitish/SEM 3/FoCP/one.txt"
file_2_path = "E:/bitish/SEM 3/FoCP/two.txt"

try:
    with open(file_1_path) as file_1:
        with open(file_2_path) as file_2:

            # Compare the contents of both files
            if file_1.read() == file_2.read():
                print(f"{file_1_path} and {file_2_path} contain the same contents")
            else:
                print("They are different")

except FileNotFoundError:
    print("File not found")
