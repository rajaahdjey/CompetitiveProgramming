import math
N , L = [int(x) for x in input().split(" ")]

for _ in range(N):
    opponent_level = int(input())
    if L > opponent_level:
        L = L+math.floor(opponent_level/2)
    elif L < opponent_level:
        L = math.floor(L/2)
    else:
        continue

print(L)