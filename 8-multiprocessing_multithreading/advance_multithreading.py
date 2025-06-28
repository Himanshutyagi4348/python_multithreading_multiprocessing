#multithreading with threadpoolexecutor
from concurrent.futures import ThreadPoolExecutor
import time

def printnum(number):
        time.sleep(2)
        return f"number : {number}"

number=[1,2,3,4,5,6]
with ThreadPoolExecutor(max_workers=6) as executor:
    results=executor.map(printnum,number)

for result in results:
    print(result)