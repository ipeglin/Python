import os
import shutil
# import admin

# if not admin.isUserAdmin():
#     admin.runAsAdmin()

EXT_AUDIO = [".wav", ".mp3", ".raw", ".wma"]
EXT_VIDEO = [".mp4", ".m4a", ".m4v", ".f4v", ".f4a", ".m4b", ".m4r", ".f4b", ".mov", ".avi", ".wmv", ".flv"]
EXT_IMAGES = [".jpeg", ".jpg", ".png", ".svg", ".gif", ".bmp"]
EXT_DOCUMENTS = [".txt", ".pdf", ".doc", ".docx", ".odt", ".html"]
EXT_EXECUTABLES = [".exe"]
EXT_ZIPFILES = [".zip"]
EXT_PYFILES = [".py"]

files = os.listdir()

# Create directories if they don't exist
DIRS = ["Audio", "Video", "Images", "Documents", "Folders", "Other", "Executables", "Zip-Files", "Python"]
if not (os.path.isdir("./Audio")):
    for d in DIRS:
        os.mkdir("./{}".format(d))

    print("Directories created successfuly.")

# Run main script
for f in files:
    name, extension = os.path.splitext(f)

    if (extension in EXT_IMAGES):
        shutil.move(f, "./Images/{}".format(f))
    elif (extension in EXT_AUDIO):
        shutil.move(f, "./Audio/{}".format(f))
    elif (extension in EXT_VIDEO):
        shutil.move(f, "./Video/{}".format(f))
    elif (extension in EXT_DOCUMENTS):
        shutil.move(f, "./Documents/{}".format(f))
    elif (extension in EXT_EXECUTABLES):
        shutil.move(f, "./Executables/{}".format(f))
    elif (extension in EXT_ZIPFILES):
        shutil.move(f, "./Zip-Files/{}".format(f))
    elif (extension in EXT_PYFILES):
        if (name == "cleanDir"):
            pass
        else:
            shutil.move(f, "./Python/{}".format(f))
    else:
        if (os.path.isdir(name)):
            if (name not in DIRS):
                shutil.move(f, "./Folders/{}".format(f))
        else:
            if (f != "cleanDir.py"):
                shutil.move(f, "./Other/{}".format(f))

print("CLEANUP COMPLETED")