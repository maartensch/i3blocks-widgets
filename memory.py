#!/usr/bin/env python
import psutil
perc=int(psutil.virtual_memory().percent)
print str(perc) + "%"
