juice_count = int(input())

orange_conc = [int(x) for x in input().split(" ")]

#
total_mix = 0.0
for i in orange_conc:
    total_mix += float(i)/juice_count

print(total_mix)