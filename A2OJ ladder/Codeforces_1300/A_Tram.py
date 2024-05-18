stop_count = int(input())

pass_count = 0
max_capacity = 0
for stop in range(stop_count):
    passengers = [int(x) for x in input().split(" ")]
    pass_count -= passengers[0]
    pass_count += passengers[1]
    if pass_count > max_capacity:
        max_capacity = pass_count

print(max_capacity)
