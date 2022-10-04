'''
Regex Version of the strip() Method
Write a function that takes a string and does the same thing as the strip() string method.
If no other arguments are passed other than the string to strip, then whitespace characters
will be removed from the beginning and end of the string. Otherwise, the characters specified
in the second argument to the function will be removed from the string.
'''
import re
text = input("Please input a string: ")
alt = input("Please input a character to remove it from the string: ")
def stripRegex(text, alt):
    if alt == "":
        regexFrt = re.sub("^\s+",str(alt),text)
        regexBck = re.sub("s+$",str(alt),regexFrt)
    else:
        regexBck = re.sub(alt,"", text)
    print(regexBck)
stripRegex(text, alt)
