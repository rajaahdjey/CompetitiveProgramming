count = int(input())
stones = input()
i = 0
actions = 0
while i < count-1:
    # print(i)
    if stones[i] == stones[i+1] :
        # print(stones)
        actions = actions + 1
    i = i + 1
    #count = count - 1

print(actions)