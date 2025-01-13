fives = 0
sevens = 0

for x in input().split():
    if int(x) == 5:
        fives += 1
    elif int(x) == 7:
        sevens += 1

if fives == 2 and sevens == 1:
    print("YES")
else:
    print("NO")