import os
import shutil
from pathlib import PurePath

# Folders with their respective file extensions
EXT = {
    "Audio": [".wav", ".mp3", ".raw", ".wma", ".ogg"], # Audio files
    "C++": [".cpp"], # C++ files
    "Documents": [".txt", ".pdf", ".doc", ".docx", ".odt", ".html"], # Document files
    "Executables": [".exe"], # Executable files
    "Images": [".jpeg", ".jpg", ".png", ".svg", ".gif", ".bmp", ".jfif", ".PNG"], # Image files
    "Installer Files": [".msi"], # Installer files
    "JavaScript": [".js", ".txs", ".json"], # JavaScript files
    "Python": [".py"], # Python script files
    "Video": [".mp4", ".m4a", ".m4v", ".f4v", ".f4a", ".m4b", ".m4r", ".f4b", ".mov", ".avi", ".wmv", ".flv"], # Video files
    "Zip-Files": [".zip"] # Zipped folders
}

def get_key(val):
    for i in EXT.items():
        if (val in i[1]):
            return i[0]

    return "NULL"

folder_names = []

for i in EXT.items():
    folder_names.append(get_key(i[1][len(i[1]) - 1]))

# Setting the parent folder of the script
parent_folder = f"{PurePath(os.path.realpath(__file__)).parents[0]}"

# Changing the directory path to the currect path of the script. This makes sure the files and dirs are created in the correct folder
os.chdir(parent_folder)

# Get the key / folder name of the extension

# List all the files in the current directory
files = os.listdir(parent_folder)

nr_dirs_created = 0
nr_moved_files = 0

# Create directories if they don't exist

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

folder_names.append("Folders")
folder_names.append("Other")

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
        if f == os.path.basename(__file__) or "git" in f or f == "Directory Cleanup.ps1":
            continue

        key = get_key(extension)

        if key != "NULL":
            # Print to console what you are moving
            print(f"MOVING '{f}'  ==>  './{key}/'")

            # Moving the file
            shutil.move(f, f"./{key}/{f}")
            nr_moved_files += 1

        if key and key not in EXT.keys():
            print(f"MOVING '{f}'  ==>  './Other/'")
            shutil.move(f, f"./Other/{f}")
            nr_moved_files += 1

    # If the item if a directory... Do this
    else:
        
        if (os.path.isdir(f"{parent_folder}/{name}")):
            if not (name in EXT.keys() and name == "Folders" and name == "Other" and "git" in f):

                if not name in folder_names:
                    
                    # Print to console what you are moving
                    print(f"MOVING '{f}'  ==>  './Folders/'")

                    # Moving the directory
                    shutil.move(f, f"./Folders/{f}")
                    nr_moved_files += 1
                

print("\n======================================")

print(f"\n\tFILES MOVED: #{nr_moved_files}")

print("\n========  CLEANUP COMPLETED  =========")

end = input("")