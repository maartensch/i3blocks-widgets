import os,json
from os.path import dirname,abspath,isfile,basename
from subprocess import check_output
from bs4 import BeautifulSoup

# Widgetmon
# 
# 1. Executes widgets in specified folders
# 2. Reads the last word of the output
# 3. Outputs the final JSON
#


# Usefull for stripping pango/html markup
def stripHtmlTags(htmlTxt):
    if htmlTxt is None:
        return None
    else:
        return ''.join(BeautifulSoup(htmlTxt,"lxml").findAll(text=True)) 

def get(paths,excludedFiles):
    d = {}
    for path in paths:
        for fpath in os.listdir(path):
            if fpath in excludedFiles: continue
            apath = path + "/" + fpath
            if isfile(apath):
                res = check_output([apath])
                res = str(res)
                res = stripHtmlTags(res)
                res = res.strip()
                bname = basename(apath).split(".")[0]
                d[bname] = res

    return json.dumps(d)
