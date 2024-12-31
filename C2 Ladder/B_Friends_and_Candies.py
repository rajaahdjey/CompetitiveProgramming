t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    tot = sum(a)
    if tot % n != 0:
        print(-1)
    else:
        tot_needed = tot / n
        ans = 0
        for i in range(n-1,-1,-1):
            if a[i] <= tot_needed:
                break
            else:
                ans += 1
        print(ans)

