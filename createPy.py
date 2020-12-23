import os
import sys

# Lambda function that clears the console
clear = lambda:os.system("cls")

# String that will contain all the wanted modules
imports = ""

# Appending the lambda function to the new file
clear_var = '\nclear = lambda:os.system("cls")'

# Add wanted standard modules you know you usually need
modules = [
    "os",
    "sys"
]

# Clearing the console
clear()

# Appending all std modules to a string
for i in modules:
    imports += "import " + i + "\n"

# Trying to use the pass system argument
try:
    # There was an stdin arg passed in the command line
    file_name = str(sys.argv[1])
except:
    # If not. Ask for the wanted name of the python file
    file_name = input("Name of the python file: ")

# If the user input .py as a part of the file name, ignore the extension
if (".py" in file_name):
    # Split the file_name string to exclude the extension
    file_name, ext = os.path.splitext(file_name)

# Opening the file in current working directory with write mode
f = open(f"{file_name}.py", "w+")

# Writing the std modules and clear lambda function to the script
f.write(imports + clear_var)

# Closing the file
f.close()

# Printing to the user that the file has been created
print(file_name, "successfully created")
