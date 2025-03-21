import math
import threading

global threads

threads = 12
start = 1
end = 2000000
countNumber = 100000
total_time = 0

def calculatePrimeNumbers(start, end):
    primeNumbers = []
    for i in range(start, end):
        if i < 2:
            continue
        prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            primeNumbers.append(i)

def countToThisNumber(n):
    square = []
    for i in range(1, n):
        k = i*i

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