#!/usr/bin/env python
import psutil
perc=int(psutil.cpu_percent(interval=1))
print(str(perc) + "%")
