##multithreading
import threading
import time
def printnum():
    for i in range (5):
        time.sleep(2)
        print(f"number : {i}")

def printletter():
    for letter in "abcde":
        time.sleep(2)
        print (f"letter {letter}")


##creating two threads for each function
t1=threading.Thread(target=printnum)
t2=threading.Thread(target=printletter)
##start the thread
t1.start()
t2.start()

##after execution join the thread to  complete i/o operation simultaneously
t1.join()
t2.join()


now=time.time()
print(now)
curr=time.time()
timetaken=curr-now
print(timetaken)
