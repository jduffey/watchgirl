import time


starttime=time.time()

while True:
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))
    print(time.time())
    print(time.time())
    print(time.time())
    print(time.time())
    print()
    