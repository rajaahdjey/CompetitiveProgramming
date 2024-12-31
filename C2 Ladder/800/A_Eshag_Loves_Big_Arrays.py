t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    first_ele = a[0]
    for i in range(1,n):
        if a[i] > first_ele:
            break
        elif i == n-1:
            i = n
            break

    print(n-i)
