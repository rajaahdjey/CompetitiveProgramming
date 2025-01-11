t = int(input())

for _ in range(t):
    n = int(input())
    enemy_pawns = list("0"+input()+"0")
    gregor_pawns = list("0"+input()+"0")
    moves = 0
    for i in range(1,n+1):
        # print(gregor_pawns,enemy_pawns,i)
        if gregor_pawns[i] == '0':
            # print("no pawns")
            continue
        if gregor_pawns[i] == '1' and enemy_pawns[i] == '0':
            # print("pawn moves up")
            moves += 1
            enemy_pawns[i] = '-1'
        elif gregor_pawns[i] == '1' and enemy_pawns[i-1] == '1':
            # print("pawn moves up and left")
            moves += 1
            enemy_pawns[i-1] = '-1'
        elif gregor_pawns[i] == '1' and enemy_pawns[i+1] == '1':
            # print("pawn moves up and right")
            moves += 1
            enemy_pawns[i+1] = '-1'
        else:
            # print("nothing happening")
            continue

    print(moves)