import time
starttime=time.time()
while True:
    print(time.time())
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))