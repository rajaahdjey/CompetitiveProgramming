status = input()

char = 0
init_team = status[0]

for player in status:
    if player == init_team:
        char += 1
    else:
        char = 1
        init_team = player
    if char == 7:
        break

if char == 7:
    print("YES")
else:
    print("NO")
    