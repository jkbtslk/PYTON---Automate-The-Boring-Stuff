#! oython3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - Deletes keyword from a shelve.
#        py.exe mcb.pyw deleteall - Deletes all keywords from a shelve.

import shelve, pyperclip, sys

mcbShelf = shelve.open("mcb")

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()

    # Delete items from a shelve.
elif len(sys.argv) == 3 and sys.argv[1].lower() == "delete":
    del mcbShelf[sys.argc[2]]
elif len(sys.argv) == 2:
# List keyword and load content.
    if sys.argc[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
# Delete all arguments.
    elif sys.argv[1].lower() == "deleteall":
        for keyword in list(mcb_shelf.keys()):
            del mcbShelf[keyword]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
