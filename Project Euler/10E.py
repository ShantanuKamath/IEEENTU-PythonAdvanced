import eulerlib
import time

def calc_sum(num):
    prime_generator = eulerlib.prime_numbers.prime_gen()
    number = next(prime_generator)
    total = 0
    while number < num:
        total+=number
        number = next(prime_generator)
    print(total)

start_time = time.time()
calc_sum(2000000)
print("--- %s seconds ---" % (time.time() - start_time))
##  --- 0.7231860160827637 seconds ---
