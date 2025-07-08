import sys
import math
a = int(sys.stdin.readline())

if a == 1:
    print("")
else:
    def isPrime(n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

    result = []
    n = a
    while not isPrime(n):
        for i in range(2, int(math.sqrt(a))+1):
            if n % i == 0 and isPrime(i):
                n = n//i
                result.append(i)
    if n != 1:
        result.append(n)
    result.sort()
    print(a if not result else '\n'.join(map(str, result)))