wooden_cupboard_count = int(input())

# check number of left open 
# check number of right open

#if left open is less than half of total , he needs to close them and vice verse
#same logic for the right open as well.
#open = 1
left_open = 0 
right_open = 0
for i in range(wooden_cupboard_count):
    door = [int(x) for x in input().split(" ")]
    if door[0]:
        left_open+=1
    if door[1]:
        right_open += 1
ans = 0

if left_open*2 > wooden_cupboard_count:
    ans += abs(left_open-wooden_cupboard_count)
else:
    ans += left_open
if right_open*2 > wooden_cupboard_count:
    ans += abs(right_open-wooden_cupboard_count)
else:
    ans += right_open
print(ans)