t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    val = n
    for i in range(1,n):
        if 2**i-1 < n:
            ans = 2**i-1
            continue
        else:
            break
    print(ans)
