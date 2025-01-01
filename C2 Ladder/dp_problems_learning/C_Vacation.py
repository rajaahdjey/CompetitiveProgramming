#my implementation

# n = int(input())

# day_wise = []

# for _ in range(n):
#     day_wise.append([int(x) for x in input().split()])



# ans = [[0] * 3 for _ in range(n)] #cannot use [[0,0,0]] * n ... shared referencecs ...

# ans[0] = day_wise[0]
# curr_activity_idx = [None]*n


# for i in range(1,n):
#     for j in range(0,3): #0,1,2
#         if j == 0:
#             ans[i][j] = max(ans[i-1][1],ans[i-1][2]) + day_wise[i][j]
#         elif j == 1:
#             ans[i][j] = max(ans[i-1][0],ans[i-1][2]) + day_wise[i][j]
#         elif j == 2:
#             ans[i][j] = max(ans[i-1][0],ans[i-1][1]) + day_wise[i][j]

# print(max(ans[n-1]))


#better implementation. 

n = int(input())
ans = [0,0,0]

for day in range(n):
    day_ans = [0,0,0]
    cost = [int(x) for x in input().split()]
    for i in range(0,3):
        for j in range(0,3):
            # print(i,j)
            if (i!=j):
                day_ans[j] = max(day_ans[j], ans[i] + cost[j])
            # print(day_ans)
    ans = day_ans

print(max(ans))

