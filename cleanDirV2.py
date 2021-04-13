import os
import shutil
from pathlib import PurePath

# Folders with their respective file extensions
EXT = {
    "Audio": [".wav", ".mp3", ".raw", ".wma", ".ogg"], # Audio files
    "Video": [".mp4", ".m4a", ".m4v", ".f4v", ".f4a", ".m4b", ".m4r", ".f4b", ".mov", ".avi", ".wmv", ".flv"], # Video files
    "Images": [".jpeg", ".jpg", ".png", ".svg", ".gif", ".bmp"], # Image files
    "Documents": [".txt", ".pdf", ".doc", ".docx", ".odt", ".html"], # Document files
    "Executables": [".exe"], # Executable files
    "Zip-Files": [".zip"], # Zipped folders
    "Python": [".py"], # Python script files
    "JavaScript": [".js", ".txs", ".json"], # JavaScript files
    "C++": [".cpp"] # C++ files
}

# Setting the parent folder of the script
parent_folder = f"{PurePath(os.path.realpath(__file__)).parents[0]}"

# Changing the directory path to the currect path of the script. This makes sure the files and dirs are created in the correct folder
os.chdir(parent_folder)

# Get the key / folder name of the extension
def get_key(val):
    for i in EXT.items():
        if (val in i[1]):
            return i[0]

    return "key doesn't exist"

# List all the files in the current directory
files = os.listdir(parent_folder)

# Create directories if they don't exist
nr_dirs_created = 0

print("\n========== CREATING FOLDERS ==========\n")

# For all folders in EXT try to create folders
for DIR in EXT.keys():
    if not (os.path.isdir(f"{parent_folder}/{DIR}")):
        print(f"CREATING '{DIR}'")
        os.mkdir(f"{parent_folder}/{DIR}")
        nr_dirs_created += 1 # Increment the number of directories created

# Create Folders dir if it doesnt exist
if not (os.path.isdir(f"{parent_folder}/Folders")):
    print(f"CREATING 'Folders'")
    os.mkdir(f"{parent_folder}/Folders")
    nr_dirs_created += 1 # Increment the number of directories created

# Create Other dir if it doesnt exist
if not (os.path.isdir(f"{parent_folder}/Other")):
    print(f"CREATING 'Other'")
    os.mkdir(f"{parent_folder}/Other")
    nr_dirs_created += 1 # Increment the number of directories created

print("\n======================================\n")

# Print to console how many directories were created
print(f"{nr_dirs_created}/{len(EXT.keys()) + 2} Directories created successfully")

print("\n============ MOVING FILES ============\n")

# Move files and folders to the correct category directory
for f in files:

    # Split the fire into names and extensions
    name, extension = os.path.splitext(f)

    # If the item is a file E.I it does have an extension
    if extension:

        # If the file is the script itself... Skip
        if f == os.path.basename(__file__):
            continue

        # Print to console what you are moving
        print(f"MOVING '{f}' TO './{get_key(extension)}/{f}'")

        # Moving the file
        shutil.move(f, f"./{get_key(extension)}/{f}")

    # If the item if a directory... Do this
    else:
        
        if (os.path.isdir(f"{parent_folder}/{name}")):
            if (name not in EXT.keys() and name != "Folders" and name != "Other"):

                # Print to console what you are moving
                print(f"MOVING '{f}' TO './Folders/{f}'")

                # Moving the directory
                shutil.move(f, f"./Folders/{f}")
        
        else:
            if (f != os.path.basename(__file__)):
                print(f"MOVING '{f}' TO './Other/{f}'")
                shutil.move(f, f"./Other/{f}")

print("\n======================================\n")

print("#####  CLEANUP COMPLETED  #####")