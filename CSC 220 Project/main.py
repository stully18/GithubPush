import timeit
from functions import threadedPrime, calculatePrimeNumbers, threads, start, end

iterations = 1

time_threaded = timeit.timeit(lambda: threadedPrime(end), number=iterations)
print(f"{threads} threads: {round(time_threaded/iterations, 4)} seconds")

time_single_thread = timeit.timeit(lambda: calculatePrimeNumbers(start, end), number=iterations) 
print(f"Single thread: {round(time_single_thread/iterations, 4)} seconds")



