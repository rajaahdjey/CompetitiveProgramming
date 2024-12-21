N , M = [int(x) for x in input().split(" ")]

gourmet_level = [int(x) for x in input().split(" ")]

deliciousness = [int(x) for x in input().split(" ")]

max_deli = max(deliciousness)

sushi_lookup = [-1]*(max_deli+1)

for person in range(len(gourmet_level)):
    if gourmet_level[person] > max_deli:
        continue
    else:
        for sushi in range(gourmet_level[person],max_deli+1):
            sushi_lookup[sushi] = person+1
        max_deli = gourmet_level[person]-1


for required_sushi in deliciousness:
    print(sushi_lookup[required_sushi])


