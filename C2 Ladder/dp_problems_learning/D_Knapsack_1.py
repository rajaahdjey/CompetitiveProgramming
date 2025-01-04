#my implementaiton

# N , W = [int(x) for x in input().split()]

# values = [0]*(W+1)

# for i in range(0,N):
#     w , v = [int(x) for x in input().split()]
#     for j in range(W,-1,-1):
#         if w+j <= W:
#             values[w+j] = max(values[j]+v , values[w+j])
#     values[w] = max(values[w],v)

# print(values[W])

#better soln : 
N , W = [int(x) for x in input().split()]
values = [0]*(W+1)

for i in range(0,N):
    w , v = [int(x) for x in input().split()]
    for j in range(W-w,-1,-1):
        values[j+w] = max(values[j+w], (values[j]+v))

print(values[W])