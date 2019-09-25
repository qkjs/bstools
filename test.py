from bstools import bsTime
import time

ts = str(time.time() * 1000)[:13]
print(ts)
print(bsTime.tsToLt(ts, splitSign = "|"))


