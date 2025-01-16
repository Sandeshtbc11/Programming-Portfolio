"""
The Unix nl command prints the lines of a text file with a line number at the start
of each line. (It can be useful when printing out programs for dry runs or white-box
testing). Write an implementation of this command. It should take the name of the
files as a command-line argument
"""
file_path = "E:/bitish/SEM 3/FoCP/one.txt"

# Creating and write some lines
with open(file_path, "w") as f:
    f.write("Sandesh\n")
    f.write("Basnet\n")
    f.write("The British College\n")
    
try:
    with open(file_path) as f:
        # Enumerate 
        for line_num, line in enumerate(f, start=1):
            print(f'{line_num}: {line}', end='')

except FileNotFoundError:
    print("File not found")