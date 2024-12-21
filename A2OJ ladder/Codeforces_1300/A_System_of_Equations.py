#a2+b = m
#a+b2 = n

m , n = [int(x) for x in input().split(" ")]

ctr = 0

for a in range(m+1):
    for b in range(n+1):
        if (a**2+b ==m) and (a+b**2 == n):
            ctr += 1

print(ctr)
