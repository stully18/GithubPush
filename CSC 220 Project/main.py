import threading
import timeit
from functions import calculatePrimeNumbers, countToThisNumber

global threads
threads = 12
start = 1
end = 10000
countNumber = 100000

def threadedPrime(end):
    chunkSize = int(end / threads)

    threadLst = []
    for i in range(threads):
        if i == 0:  # First iteration
            start = 1
            end = chunkSize
        else:
            start = i * chunkSize
            end = (i + 1) * chunkSize
        thread = threading.Thread(target=calculatePrimeNumbers, args=(start, end)) 
        threadLst.append(thread)
    for i in threadLst:
        i.start()
    for i in threadLst:
        i.join()

def threadedCount(countNumber):
    global threads
    chunkSize = int(countNumber / threads)
    threadLst = []
    for i in range(threads):
        if i == 0:  # First iteration
            start = 1
            end = chunkSize
        else:
            start = i * chunkSize
            end = (i + 1) * chunkSize
        thread = threading.Thread(target=calculatePrimeNumbers, args=(start, end)) 
        threadLst.append(thread)
    for i in threadLst:
        i.start()
    for i in threadLst:
        i.join()

iteration = 10
total_time = 0

for i in range(iteration):
    time_threaded = timeit.timeit(lambda: threadedPrime(end), number=1)
    print(f"Time iteration {i}: {round(time_threaded, 4)} seconds")
    total_time += time_threaded

average_time = total_time / iteration

print(f"{threads} threads: {round(average_time, 4)} seconds")

print(f"{threads} threads: {round(time_threaded, 4)} seconds")

time_single_thread = timeit.timeit(lambda: calculatePrimeNumbers(start, end), number=1) 
print(f"Single thread: {round(time_single_thread, 4)} seconds")



