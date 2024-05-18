input_str = input()
lucky = 0
for i in input_str:
    if i == "4":
        lucky+= 1
    elif i =="7":
        lucky += 1
    else:
        continue

if lucky == 4 or lucky == 7:
    print("YES")
else:
    print("NO")