'''
REAL WORLD EXAMPLE-->multiprocessing for cpu bound
SCENERIO-->Factorial calculation
especialy with large number ,with the help of multiprocessing it is used to distribute the work load across multiple cpu cores and improve performance'''

from concurrent.futures import ProcessPoolExecutor
import math
import sys
import time
#increase the maximum number of didgit for integer conversion
sys.set_int_max_str_digits(100000)

##function to compute factorial
def compute_factorial(number):
    print(f"factorial of {number}")
    result=math.factorial(number)
    print(f"the factorial of {number} is {result}")
    return result


if __name__=="__main__":
    numbers=[200,600,700,8000]
    start_time=time.time()
    with ProcessPoolExecutor(max_workers=4) as pool:
        results=pool.map(compute_factorial,numbers)

    end_time=time.time()
    print(f"results {results}")
    print(f"time taken {end_time-start_time} second")


