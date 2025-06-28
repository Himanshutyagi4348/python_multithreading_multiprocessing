###multiprocessing
'''process that are ren in parrallel to perform i/o operation more efficiently '''
##parallel execution
'''when we want to use multiple core of the cpu'''
import multiprocessing
import time 
def countsquare():
    for i in range(5):
        time.sleep(1)
        print(f"square: {i*i}")

def countcube():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube: {i*i*i}")
##creating two process
if __name__=="main":
    p1=multiprocessing.Process(target=countsquare)
    p2=multiprocessing.Process(target=countcube)
    t=time.time()

##initializing the processes
    p1.start()
    p2.start()

##wait for processes to complete
    p1.join()
    p2.join()
    finishtime=time.time-t
    print(finishtime)