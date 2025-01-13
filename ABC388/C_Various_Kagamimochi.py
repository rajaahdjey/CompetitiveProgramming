N = int(input())

sizes = [int(x) for x in input().split()]

ans = 0

# i need to find point where k is more than or equal to twice of sizes[i]

def binary_search(array,left,right,s):

    l , r = 0 , len(array)-1
    while l <= r :
        # print(l,r)
        mid = l + (r-l)//2
        # print(mid)
        if 2 * s <= array[mid] :
            r = mid -1 
        else:
            l = mid+1
    return len(array)-l

for i in range(N):
    step_ans = binary_search(sizes,i,N,sizes[i])

    if step_ans>0:
        ans += step_ans
    else:
        ans += 0

print(ans)


