t = int(input())

for _ in range(t):
    n = int(input())
    nums = [int(x) for x in input().split()]

    print(max(nums)-min(nums))