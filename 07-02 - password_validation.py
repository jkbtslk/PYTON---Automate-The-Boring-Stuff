'''
Strong Password Detection
Write a function that uses regular expressions to make sure the password string it is passed is strong.
A strong password is defined as one that is at least eight characters long, contains both uppercase and
lowercase characters, and has at least one digit. You may need to test the string against multiple regex
patterns to validate its strength.
'''

import re
password = input("Please enter a password: ")

passwordRegex = re.compile(r'[a-zA-Z0-9]{8,}')

if passwordRegex.search(password):
    print('Strong password!')
else:
    print("Weak password!")

