friends = int(input()) + 1
fingers = 0
for x in input().split(" "):
    fingers += int(x)

ways = 0
for i in range(1,6): #1 to 5 fingers
    if (fingers + i)% friends != 1 :
        ways += 1

print(ways)
