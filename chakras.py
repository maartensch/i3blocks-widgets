# -*- coding: utf-8 -*-

import random
import sys


class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    ORANGE = '\033[93m'
    YELLOW = '\033[93m'
    INDIGO = '\033[95m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class colors:
    BLUE = '<span color="blue">'
    GREEN = '<span color="green">'
    RED = '<span color="red">'
    ORANGE = '<span color="orange">'
    YELLOW = '<span color="yellow">'
    INDIGO = '<span color="purple">'
    END = '</span>'

lines = []
lines.append(colors.RED + '@root' + colors.END)
lines.append(colors.ORANGE + '@feel' + colors.END)
lines.append(colors.YELLOW + '@conf' + colors.END)
lines.append(colors.GREEN + '@love' + colors.END)
lines.append(colors.BLUE + '@talk' + colors.END)
lines.append(colors.INDIGO + '@3rdy' + colors.END)
lines.append(colors.INDIGO + '@crwn' + colors.END)

def random_line(lines):
    myline =random.choice(lines)
    return myline

print(random_line(lines))
