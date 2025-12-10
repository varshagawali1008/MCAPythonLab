import threading
def show_number(n):
    print("number",n)

threads=[]

for i in range(5):
    t=threading.Thread(target=show_number,args=(i,))
    threads.append(t)
    t.start()

#for t in threads:
    t.join()
