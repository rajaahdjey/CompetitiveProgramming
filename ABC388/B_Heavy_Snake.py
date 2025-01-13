N , D = [int(x) for x in input().split()]

T = []
L = []

for _ in range(N):
    thick , length = [int(x) for x in input().split()]
    T.append(thick)
    L.append(length)



for k in range(1,D+1):
    ans = 0
    for i in range(N):
        ans = max(ans,T[i]*(L[i]+k))
    print(ans)