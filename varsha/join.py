import threading
def greet(name):
    print("hello",name)

t1=threading.Thread(target=greet,args=("varsha",))
t2=threading.Thread(target=greet,args=("pratiksha",))

t1.start()
t2.start()

t1.join()
t2.join()