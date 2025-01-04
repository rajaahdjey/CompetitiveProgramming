s = input()
t = input()

dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]



for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j] :
            # print(f"At {i}{j} , {s[i]} is same as {t[j]}")
            dp[i+1][j+1] = max(dp[i+1][j+1] , dp[i][j] + 1)
        else:
            dp[i+1][j+1] = max(dp[i][j] ,dp[i+1][j],dp[i][j+1])

ans = ""

# for row in dp:  
#     print(row)

sidx = len(s)
tidx = len(t)
res = []
while sidx>0 and tidx>0:
    if s[sidx-1] == t[tidx-1]:
        res.append(s[sidx-1])
        sidx-=1
        tidx-=1
    else:
        if dp[sidx][tidx] == dp[sidx-1][tidx]:
            sidx-=1
        else:
            tidx-=1
# print(res)
res=res[::-1]
print(''.join(res))




