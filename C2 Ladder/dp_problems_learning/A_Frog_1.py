# my initial solution - hardcoded the 2nd val and then started comparison... 

# n = int(input())

# heights = [int(x) for x in input().split()]

# ans = [0]

# ans.append(abs(heights[1]-heights[0]))

# for i in range(2,n):
#     ans.append(min(abs(heights[i]-heights[i-1])+ans[i-1],abs(heights[i]-heights[i-2])+ans[i-2]))

# print(ans[-1])

#better solution , no hardcoding. 
n = int(input())
heights = [int(x) for x in input().split()]
ans = [float('inf')] * n
ans[0] = 0

for i in range(0,n):
    for j in range(i+1,i+3):
        if (j<n):
            ans[j] = min(ans[j] , ans[i]+ abs(heights[i]-heights[j]))

print(ans[n-1])