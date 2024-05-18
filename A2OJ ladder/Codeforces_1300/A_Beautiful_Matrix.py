sol = 0 
for i in range(0,5):
    mat = [int(x) for x in input().split(" ")]
    for j in range(0,5):
        if mat[j]:
            sol += abs(2-i)
            sol += abs(2-j)
            print(sol)
            break