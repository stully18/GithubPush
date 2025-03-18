def calculatePrimeNumbers(start, end):
    primeNumbers = []
    for i in range(start, end):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
        if prime:
            primeNumbers.append(i)

def countToThisNumber(n):
    square = []
    for i in range(1, n):
        k = i*i