no_of_soldiers = int(input())
order = [int(x) for x in input().split(" ")]

#logic: 
#only first and last nos are important 
#if the max and min are not leftmost and rightmost respectively, they can be swapping one by one in neighboring.
#time taken for one swap = one second. so we need to count number of moves, which is equal to number of seconds. 

min_pos = 0
max_pos = 0
#height can vary from 1 to 100
min_height = 101
max_height = 0

for pos,soldier in enumerate(order):
    if soldier > max_height: #bias towards soldier already towards left
        max_height = soldier
        max_pos = pos
    if soldier <= min_height : #bias towards soldier towards right.
        min_height = soldier
        min_pos = pos

# print(min_pos,min_height,max_pos,max_height)

if max_pos > min_pos :
    print(  max_pos + (no_of_soldiers-1-min_pos) - 1  )
else:
    print(  max_pos + (no_of_soldiers-1-min_pos) )
