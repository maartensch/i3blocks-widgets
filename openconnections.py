#!/usr/bin/python
__author__ = 'sword'

from subprocess import CalledProcessError,check_output
try:
    r = check_output(['lsof','-i','-P','-n'])
    lines = r.splitlines()
    apps = []
    for i in range(0,len(lines)):
        if(i != 0):
            app = lines[i].split(' ')[0].title()
            if app not in apps:
                apps.append(app)

    print "[" + ",".join(apps) + "]"
except CalledProcessError:
    print "None"
