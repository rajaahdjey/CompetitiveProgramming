s , n = [int(x) for x in input().split(" ")]

str_bonus = []

for i in range(n):
    strength , bonus = [int(x) for x in input().split(" ")]
    str_bonus.append((strength,bonus))



for strength,bonus in sorted(str_bonus, key = lambda ele: (ele[0],ele[1])):
    if s > strength:
        s += bonus
    else:
        s = -1
        break

if s == -1:
    print("NO")
else:
    print("YES")

