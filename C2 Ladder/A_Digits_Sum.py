t = int(input())

for _ in range(t):
    n = int(input())
    ans = n//10 
    if n % 10 == 9:
        ans += 1
    print(ans)
