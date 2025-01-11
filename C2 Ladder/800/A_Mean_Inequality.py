t = int(input())

for _ in range(t):
    n = int(input())
    nums = [int(x) for x in input().split()]

    nums.sort()
    small_ele = nums[0:n]
    large_ele = nums[n:]
    final_array = [0] * (2*n)
    
    for i in range(2*n):
        if (i+1) % 2 == 0:
            final_array[i] = large_ele[i//2]
        else:
            final_array[i] = small_ele[i//2]
    
    print(*final_array)