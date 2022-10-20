#! python3
# selectiveCopy.py - a program that walks through a folder tree
# and search for files with a certain file extension.
# Copy these files from whatever location they are in to a new folder.
import os, shutil

# Get a path and extension from the user.
p = input("Please input an absolute path: ")
extension = ".rtf"

# Change working directory to path provided by the user.
# Create a new destination folder and get its absolute path.
os.chdir(p)
os.mkdir("Copies")
newPath = os.path.abspath("Copies")

# Walk through all directories, subdirectories and search for files with extension provided
# by the user.
for foldername, subfolders, filenames in os.walk(p):
    for file in filenames:
        if file.endswith(extension):
            # Retrieve absolute paths of files found and copy them to destination folder.
            filePath = os.path.abspath(file)
            shutil.copy(filePath, newPath)
            print("Copying --->", file)
            print()
print("All files with extension /",extension,"/ have been successfuly copied  to a folder ", newPath)
