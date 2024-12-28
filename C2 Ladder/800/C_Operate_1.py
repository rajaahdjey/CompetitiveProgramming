n = int(input())
first_str = input()
second_str = input()
fsl = len(first_str)
ssl = len(second_str)
poss = True

#3 operations possible are
#insert any one character at any position, including beginning or end.
#delete one character from S
#choose one character from S and replace with another character.

#k is always 1 

if first_str == second_str:
    poss = True
elif abs(fsl - ssl) > 1:
    poss = False
elif fsl - ssl == 1:
    i = 0
    ctr = 0
    while i < ssl:
        if first_str[i] != second_str[i]:
            ctr += 1
            break
        i = i+1
    if first_str[i+1:] == second_str[i:]:
        poss = True
    else:
        poss = False
elif fsl - ssl == -1:
    i = 0
    ctr = 0
    while i < fsl:
        if first_str[i] != second_str[i]:
            ctr += 1
            break
        i = i+1
    if first_str[i:] == second_str[i+1:]:
        poss = True
    else:
        poss = False
else:
    i = 0
    ctr = 0
    while i < fsl:
        if first_str[i] != second_str[i]:
            ctr += 1
        if ctr > 1:
            poss = False
            break
        else:
            poss = True
        i = i+1


if poss:
    print("Yes")
else:
    print("No")