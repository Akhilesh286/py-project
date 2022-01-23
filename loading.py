import itertools
import threading
import time
import sys
done = False
#here is the animation
def animate():
    a="#"
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        a+=f'{a}#'
        sys.stdout.write('\rloading[ ' +a+']')
        sys.stdout.flush()
        time.sleep(0.1)
        if a == "#####":
            break
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(10)
done = True