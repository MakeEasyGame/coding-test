import math
a = int(input())
lst = map(int, input().split())
result = 0
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for i in lst:
    if isPrime(i):
        result+=1
print(result)