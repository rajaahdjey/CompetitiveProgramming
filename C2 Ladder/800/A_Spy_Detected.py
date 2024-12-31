t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    match_ele = a[0]
    change = None
    ctr = 0
    for i in range(n):
        if a[i]!=match_ele:
            ctr += 1
            change = i
            match_ele = a[i]
    
    if ctr == 1:
        print(change+1)
    else:
        print(change)
