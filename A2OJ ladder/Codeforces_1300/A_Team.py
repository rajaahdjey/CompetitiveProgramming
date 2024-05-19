n = int(input())

ctr = 0
for i in range(0,n):
    knows = 0
    for x in input().split(" "):
        knows += int(x)
    if knows > 1: 
        ctr += 1
print(ctr)