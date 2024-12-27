n , m = [int(x) for x in input().split(" ")]

f = [int(x) for x in input().split(" ")]


f.sort()

min_diff = None
for i in range(m-n+1):
    diff = f[i+n-1]-f[i]
    if min_diff is None or diff < min_diff:
        min_diff = diff

print(min_diff)



