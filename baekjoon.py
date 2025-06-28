a = int(input())
result = 0

for i in range(a):
    s = str(i)
    n = i
    for j in s:
        n+=int(j)
    
    if n == a:
        result = i
        break

print(result)