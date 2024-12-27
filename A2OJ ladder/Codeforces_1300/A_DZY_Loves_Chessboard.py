n,m = [int(x) for x in input().split(" ")]

status_string = []

result_string = []

for _ in range(n):
    status_string.append(input())
# . is good
# - is bad

last_used_char = "W"

for i in range(len(status_string)):
    row = ""
    for j in range(len(status_string[i])):
        if status_string[i][j] == '-': #bad
            row += "-"
            continue
        else:
            if i>0:
               if result_string[i-1][j] != "-":
                last_used_char = result_string[i-1][j] 
            if last_used_char == "W":
                row += "B"
                last_used_char = "B"
            else:
                row += "W"   
                last_used_char = "W"   
    result_string.append(row)

for row in result_string:
    print(row)
