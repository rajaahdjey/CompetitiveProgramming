n_lines = int(input())
val = 0
for i in range(n_lines):
    statement = input()
    if statement[0] == "X": #find if X is first
        if statement[1:3] == "++":
            val += 1
        else:
            val += -1
    elif statement[0:2] == "++" : #these covers where X is last
        val += 1
    else: #this is --X
        val -= 1

print(val)