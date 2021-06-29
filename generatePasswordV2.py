from os.path import exists
import hashlib
import random
import sys
import os

# Lambda function that clears the console
clear = lambda:os.system("cls")

# Returns a hashed string using SHA256
def hash_string(string):
    return hashlib.sha256(str(string).encode("utf-8")).hexdigest()

# Function that gets the password length input from the user
def password_length():
    try:
        length = int(input("\nNB! The password should be at least 8 characters long\nPassword length: "))
        if (length < 8): raise Exception("The password length is too short")
        
        return length
    except Exception as error:
        return password_length()

# Creating a password which is randomized based on letters and numbers
def create_password(length):
    options = get_characters()
    password = []
    for i in range(0, length):
        password.append(random.choice(options))
    return "".join(password)

# Function that returns an array of all the valid characters for passwords
def get_characters():
    array = []
    excluded_characters = ['"', "'", ",", ".", "/", "<", ">", ":", ";", "\\", "(", ")" "[", "]", "{", "}"] # Characters that are not allowed in the password

    for i in range(33, 123): 
        if (chr(i) in excluded_characters): continue # If the character is in the array of the excluded characters
        array.append(chr(i))

    return array

# Function that decides the filepath and returns s
def get_file_path():
    file = f"{os.path.expanduser('~')}" # Setting the file path to the users home folder
    
    if (exists(f"{file}\Documents")): file = file + "\Documents" # If the 'Document' folder exists then add this to the path
    elif (exists(f"{file}\Dokumenter")): file = file + "\Dokumenter"
    file = f"{file}\genPass.txt" # Add the file name to the path
    return file

# A function that writes in a service name and a hashed password to a specific file
def write_to_file(service, hashed_password, file_path):
    f = open(file_path, "a")
    f.write(f"{service}: {hashed_password}\n")
    f.close()

# Function that gets sys arguments if the program is called from the terminal
def get_sys_args():
    # Get the sys argv variables if they have been passed into the terminal
    try:
        service = sys.argv[1]
        length = int(sys.argv[2])
        return [service, length]
    except:
        return  []

# Main function
def main():
    clear()
    if (get_sys_args()):
        [service, length] = get_sys_args() # If system arguments are passed, declare service and length variables
    else:
        service = input("Which service is the password for? ")
        length = password_length()

    password = create_password(length)
    write_to_file(service, hash_string(create_password(length)), get_file_path()) # Call the write_to_file function to store the new password
    print(f"{service} ({len(password)}): {password}") # Print the password to the terminal so that you can get a glance of it

main()