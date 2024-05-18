beginning_lights = [[1, 1, 1], 
                    [1, 1, 1], 
                    [1,1, 1]]


current_lights = [input().split(" ")]
current_lights.append(input().split(" "))
current_lights.append(input().split(" "))
for i,row in enumerate(current_lights):
    for j,col in enumerate(row):
        beginning_lights[i][j] = int(not(beginning_lights[i][j])) if (int(col)%2 == 1) else (beginning_lights[i][j])
        if i < 2:
            beginning_lights[i+1][j] = int(not(beginning_lights[i+1][j])) if (int(col)%2 == 1) else (beginning_lights[i+1][j])
        if j < 2:
            beginning_lights[i][j+1] =  int(not(beginning_lights[i][j+1])) if (int(col)%2 == 1) else (beginning_lights[i][j+1])
        if i > 0:
            beginning_lights[i-1][j] =  int(not(beginning_lights[i-1][j])) if (int(col)%2 == 1) else (beginning_lights[i-1][j])
        if j > 0:
             beginning_lights[i][j-1] =  int(not(beginning_lights[i][j-1])) if (int(col)%2 == 1) else (beginning_lights[i][j-1])

for row in beginning_lights:
    print("".join(str(x) for x in row))
 