import time
starttime=time.time()
import widgetmon
import lib.widgetmonlib as widgetmonlib


while True:
    print widgetmonlib.get(widgetmon.paths,widgetmon.excludedFiles)
    time.sleep(10.0 - ((time.time() - starttime) % 10.0))
