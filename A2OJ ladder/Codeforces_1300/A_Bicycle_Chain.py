n_pedal = int(input())

pedal_teeth = [int(x) for x in input().split(" ")]

n_rearwheel = int(input())

rearwheel_teeth = [int(x) for x in input().split(" ")]

max_ratio = 0
ctr = 0 

for i in pedal_teeth:
    for j in rearwheel_teeth:
        if j%i == 0:
            if j/i > max_ratio:
                max_ratio = j/i
                ctr = 1
            elif j/i == max_ratio:
                ctr += 1

print(ctr)