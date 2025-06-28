from concurrent.futures import ProcessPoolExecutor
import time

def printsquare(number):
    time.sleep(1)
    return f"square: {number*number}"
number=[1,2,3,4,5,6,7,8,9]
##entry point of the process
if __name__=="__main__":

    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(printsquare,number)

    for result in  results:
        print(result)