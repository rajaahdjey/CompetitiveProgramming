input_vals = input().split(" ")
length = int(input_vals[0])
time = int(input_vals[1])
init_line = list(input())
while time > 0 :
    i = 0
    while i < length - 1 :
        #print(init_line)
        if init_line[i] == "B" and init_line[i + 1] =="G":
            init_line[i] = "G"
            init_line[i + 1] = "B"
            i += 1
        i = i + 1
    time = time - 1
print("".join(init_line))
