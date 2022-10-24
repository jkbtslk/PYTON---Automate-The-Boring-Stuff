#! python
"""
Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on,
in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.
"""
import os, fnmatch

path = input("Please input the path: ")
prefix = input("Please input the prefix: ")
search = prefix + "*"
files = [file for file in os.listdir(path) if fnmatch.fnmatch(file, search)]
files = sorted(files)
newString = str(prefix) + '{:0>3}.txt'
newFilenames = [newString.format(number+1) for number in range(len(files))]

for count, filename in enumerate(os.listdir(path)):
    dst = f"{prefix} {str(count)}.txt"
    src = f"{path}/{filename}"
    dst = f"{path}/{dst}"

    os.rename(src, dst)
