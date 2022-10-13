
"""
Regex Search
Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression.
he results should be printed to the screen.
09-02 - regex_search.py
"""

09-02 - regex_search.py
import os, re
# Gather user's path and regex.
pathUser = input("Please input a path: ")
regex = input("Please input a regex: ")

def searchText(pathUser):
    # Change directory to user's path and create a list containing all files and directories inside.
    os.chdir(pathUser)
    listdir = os.listdir()
    files = listdir
    # print(files)

    # For every file and directory in the list "files", please extract the absolute path. If it's a directory,
    # run searchText() inside this directory. And if it's a file, proceed with searchText().
    for file in files:
        abs_path = os.path.abspath(file)
        if os.path.isdir(abs_path):
            searchText(abs_path)
        if os.path.isfile(abs_path):

            # Open each file and search for user's input.
            with open(file, 'r', encoding='utf-8') as f:
                if regex in f.read():
                    final_path = os.path.abspath(file)
                    print("\"",regex,"\""" was found in this path " + final_path)
                else:
                    print("No match found in " + abs_path)


searchText(pathUser)
