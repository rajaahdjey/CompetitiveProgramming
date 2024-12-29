t = int(input())

for _ in range(t):
    n = int(input())
    tot = sum(int(x) for x in input().split())
    if  tot <= 0:
        print(1)
    elif tot>=n:
        print(tot-n)
    else:
        print(1)


    