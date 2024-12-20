n_houses , m_tasks = [int(x) for x in input().split(" ")]

house_list = [int(x) for x in input().split(" ")]

#total n
num_steps = 0
curr_house = 1
for i in range(m_tasks):
    # print("Steps so far:",num_steps)
    # print(f"Moving from house {curr_house} to house {house_list[i]}")
    if house_list[i] - curr_house > 0:
        num_steps += (house_list[i] - curr_house)
    elif house_list[i] - curr_house == 0:
        continue
    else:
        num_steps += ((n_houses - curr_house) + house_list[i])
    curr_house = house_list[i]

print(num_steps)