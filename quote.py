import random
import sys

def random_line(afile):

    lines = open(afile).read().splitlines()
    myline =random.choice(lines)
    return myline

if __name__ == "__main__":
    if len(sys.argv) == 2:

        fname = sys.argv[1]
        print(random_line(fname))
