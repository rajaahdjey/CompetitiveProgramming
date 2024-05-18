n = int(input())
total = [0,0,0]
for i in range(0,n):
    vect = input().split(" ")
    total = [total[x]+int(vect[x]) for x in range(0,3)]

if any(total):
    print("NO")
else:
    print("YES")