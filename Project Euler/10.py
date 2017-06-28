# Note : range is actually a generator in Python 3.
# Use xrange in Python 2.7
import math
import time

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for divisor in range(3,int(math.sqrt(number)+1),2):
            if number % divisor == 0:
                return False
        return True
    return False

def calc_sum():
    total = 0
    for num in range(1, 2000000):
        if is_prime(num):
            total+= num

    print(total)

start_time = time.time()
calc_sum()
print("--- %s seconds ---" % (time.time() - start_time))
## --- 8.055869817733765 seconds ---
