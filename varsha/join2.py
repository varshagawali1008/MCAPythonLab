import threading
import time 

def work():
    print("thread starting ")
    time.sleep(2)#pretend we are waiting for something
    print("thread done")
t1=threading.Thread(target=work)
t2=threading.Thread(target=work)

t1.start()
t2.start()

t1.join()
t2.join()
print("all threads finished")