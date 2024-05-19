array_len = int(input())

array = [int(x) for x in input().split(" ")]
num_queries = int(input())
ele_needed = [int(x) for x in input().split(" ")]


map_ele = dict()
for i,num in enumerate(array):
    map_ele[num] = i

ascending = 0
descending = 0
for ele in ele_needed:
    ascending += map_ele[ele]+1
    descending += (len(array) - map_ele[ele])

print(ascending,descending)