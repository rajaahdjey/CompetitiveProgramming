t = int(input())

for _ in range(t):
    sticks = [int(x) for x in input().split()]
    sticks.sort()
    if sticks[0] + sticks[1] == sticks[2]:
        print("YES")
    elif sticks[1] == sticks[2] :
        if sticks[0] % 2 == 0:
            print("YES")
        else:
            print("NO")
    elif sticks[0] == sticks[1]:
        if sticks[2] % 2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
