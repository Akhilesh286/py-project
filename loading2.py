import time
import sys
import os
a = "#"
for i in range(5):
    #print(a)
    sys.stdout.write(f"\rloding...[{a}]")
    sys.stdout.flush()
    a+="#"
    time.sleep(.75)