n , k = [int(x) for x in input().split()]

heights = [int(x) for x in input().split()]

costs = [float('inf')] * n

costs[0] = 0

for i in range(0,n):
    for j in range(i+1,i+k+1):
        if j < n :
            costs[j] = min(costs[j],costs[i]+abs(heights[i]-heights[j]))

print(costs[-1])