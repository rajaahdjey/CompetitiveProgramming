t = int(input())

for _ in range(t):
    n,m,k = [int(x) for x in input().split()]
    dp = [[0]*(m+2) for _ in range(n+2)]
    # print(dp)
    dp[1][1] = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i+1][j] = dp[i][j] + j
            dp[i][j+1] = dp[i][j] + i
    # for row in dp:
    #     print(row)
    
    if dp[n][m] == k:
        print("YES")
    else:
        print("NO")

    