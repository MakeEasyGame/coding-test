import math

a = int(input())
b = int(input())
lst = []
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for i in range(a, b+1):
    if isPrime(i):
        lst.append(i)

if len(lst) > 0:
    print(sum(lst))
    print(lst[0])
else:
    print(-1)