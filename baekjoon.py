import math
a = int(input())

for i in range(a):
    a, b = map(int, input().split())
    print(math.lcm(a, b))