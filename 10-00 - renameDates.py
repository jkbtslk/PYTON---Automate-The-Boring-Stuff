import re, os, shutil
from pathlib import Path

# Create a regex for American-style dates.
dateRegex = re.compile(r"""(.*?) # All text before the date
((0|1)?\d)-                      # One or two digits for the month
((0|1|2|3)?\d)-             # One or two digits for the day
((19|20)\d\d)                    # four digits after the date
(.*?)$                           # all text after the date
""", re.VERBOSE)

# Loop over the files in the working directory.
for AmerDate in os.listdir("."):
    mo = dateRegex.search(AmerDate)
# Skip files without a date.
    if mo == None:
        continue
# Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

# Form the European-style filename.
    EuroDate = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPart

# Get the full, absolute file paths.
    absWorkingDir = os.path.abspath(".")
    AmerDate = os.path.join(absWorkingDir, AmerDate)
    EuroDate = os.path.join(absWorkingDir, EuroDate)

# Rename the files.
    print(f'Renaming "{AmerDate}" to {EuroDate}"...')
    shutil.move(AmerDate, EuroDate)
