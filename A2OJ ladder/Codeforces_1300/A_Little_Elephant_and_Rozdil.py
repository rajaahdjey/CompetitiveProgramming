num_towns = int(input())
town_travel_times = [int(x) for x in input().split(" ")]

min_travel = town_travel_times[0]
min_town = 1
min_travel_prev = 0

#did not want to sort because i just need the 2 lowest values here.

for town,time in enumerate(town_travel_times[1:]):
    if time <= min_travel:
        min_town = town+2
        min_travel_prev = min_travel
        min_travel = time

    else:
        continue

if min_travel_prev != min_travel:
    print(min_town)
else:
    print("Still Rozdil")