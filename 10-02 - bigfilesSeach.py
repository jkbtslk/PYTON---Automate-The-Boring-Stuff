#!python
"""
Write a program that walks through a folder tree and searches for exceptionally large files or folders—say,
 ones that have a file size of more than 100MB. (Remember that to get a file’s size,
 you can use os.path.getsize() from the os module.) Print these files with their absolute path to the screen.
"""
import os, sys
# Get a path and a threshold from the user.
path = input("Please input a path: ")
threshold = int(input("Please input a threshold in bytes: "))
notFound = True
for foldername, subfolders, filenames in os.walk(path):
    for file in filenames:
        if os.path.getsize(os.path.join(foldername, file)) > threshold:
            print("Big file found -> ", os.path.abspath(file), "---", os.path.getsize(os.path.join(foldername, file)))
            notFound = False
if notFound:
    print("There are no files bigger than the threshold!")
