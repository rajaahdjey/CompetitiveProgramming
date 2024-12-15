soldiers_count = int(input())

soldiers_heights = [int(x) for x in input().split(" ")]

min_diff = 10000
min_a = 0
min_b = 1

for i in range(1,soldiers_count):
    diff = abs(soldiers_heights[i]-soldiers_heights[i-1])
    # print(diff)
    if diff < min_diff :
        min_diff = diff
        min_a = i
        min_b = i+1
    
if abs(soldiers_heights[0]-soldiers_heights[soldiers_count-1]) < min_diff:
    min_a = 1
    min_b = soldiers_count
    
print(min_a,min_b)
