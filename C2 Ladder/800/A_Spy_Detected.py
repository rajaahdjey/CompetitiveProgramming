t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    p1 , n1 = 0 , 0
    p2 , n2 = 0 , 0
    for i in range(n):
        if a[0] == a[i]:
            n1 += 1
            p1 = i
        else:
            n2 += i
            p2 = i

    if n1 == 1:
        print(p1+1)
    else:
        print(p2+1)