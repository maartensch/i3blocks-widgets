from subprocess import check_output
from subprocess import CalledProcessError
try:
    r = check_output(['lsof','-i','-P'])
    lines = r.splitlines()
    apps = []
    for i in range(0,len(lines)):
        if(i != 0):
            app = lines[i].split(' ')[0].title()
            app = app[:4]
            if app not in apps:
                apps.append(app)

    print "[" + ",".join(apps) + "]"
except CalledProcessError:
    print "None"
