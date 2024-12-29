n = int(input())

potions = [int(x) for x in input().split()]

stored = {}

for i in range(0,n+1):
    for j in range(0,n+1):
        stored[(i,j)] = 0
stored[(0,0)] = 0

if potions[0] > 0:
    stored[(0,1)] = potions[0]
else:
    stored[(0,1)] = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if potions[i-1] + stored[(i-1,j-1)] >= 0:
            stored[(i,j)] = max(stored[(i-1,j-1)]+potions[i-1] , stored[(i-1,j)])
        else:
            stored[(i,j)] = stored[(i-1,j)]

print(stored)