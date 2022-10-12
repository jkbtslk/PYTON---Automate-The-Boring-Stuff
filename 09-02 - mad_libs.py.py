""""
Mad Libs
Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.

The program would find these occurrences and prompt the user to replace them.

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck

The following text file would then be created:

The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.

The results should be printed to the screen and saved to a new text file.

1. Reads a file.
2. Gets input from the user.
3. Replaces string.
4. Writes a file.

"""
import re

# Open a file and create list containing words from the file.
file = open("text.txt", "r")
content = file.read()
wordsList = list(content.split())
file.close()

# Create a regex for adjectives, nouns, adverbs and verbs.
adjectiveRegex = re.compile(r"ADJECTIVE")
nounRegex = re.compile(r"NOUN")
adverbRegex = re.compile(r"ADVERB")
verbRegex = re.compile(r"VERB")

# Find regex matches and replace text.
file = open("text.txt", "w")
for word in wordsList:
    if adjectiveRegex.match(word):
        word = adjectiveRegex.sub(input("Please input an adjective: "), word)
    elif nounRegex.match(word):
        word = nounRegex.sub(input("Please input an noun: "), word)
    elif adverbRegex.match(word):
        word = adverbRegex.sub(input("Please input an adjective: "), word)
    elif verbRegex.match(word):
        word = verbRegex.sub(input("Please input an adjective: "), word)
    file.write(word)

file.close()
