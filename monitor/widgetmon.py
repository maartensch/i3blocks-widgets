import os,json
from os.path import dirname,abspath,isfile,basename
from subprocess import check_output
from bs4 import BeautifulSoup

import lib.widgetmonlib as widgetmonlib

# Widgetmon
# 
# 1. Executes widgets in specified folders
# 2. Reads the last word of the output
# 3. Outputs the final JSON
#

excludedFiles = [".gitignore","README.md","LICENSE"]

paths = []

# You can change/add a path to your (custom) widgets)
paths.append(dirname(dirname(abspath(__file__))))

if __name__ == "__main__":
    print widgetmonlib.get(paths,excludedFiles)
