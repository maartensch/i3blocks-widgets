#!/usr/bin/python

__author__ = 'sword'

from subprocess import CalledProcessError,check_output
import sys

try:
    r = check_output(['lsof','-i','-P','-n'])
    r = r.decode('ascii')
    lines = r.splitlines()
    apps = []
    for i in range(0,len(lines)):
        if(i != 0):
            app = str(lines[i]).split(' ')[0].title()
            if app not in apps:
                apps.append(app)

    data = "[" + ",".join(apps) + "]"
except CalledProcessError:
    data = "None"

print(data)
