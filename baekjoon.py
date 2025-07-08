import math
while(True):
    a = int(input())
    if a == -1:
        break
    lst = []
    for i in range(1, int(math.sqrt(a))+1):
        if a % i == 0:
            lst.append(i)
            if a//i != a:
                lst.append(a//i)
    lst.sort()
    if a == sum(lst):
        print(a, '=', ' + '.join(map(str, lst)))
    else:
        print(a, 'is NOT perfect.')