num = input()

pos = 0

while pos < len(num):
    # print("Position:",pos)
    # print("Checking:",num[pos:pos+3])
    # print("Checking:",num[pos:pos+2])
    # print("Checking:",num[pos])
    if num[pos:pos+3] == "144":
        pos = pos+3
    elif num[pos:pos+2] == "14":
        pos = pos+2
    elif num[pos] == "1":
        pos = pos+1
    else:
        break

if pos == len(num):
    print("YES")
else:
    print("NO")
    