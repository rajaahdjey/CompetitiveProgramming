t = int(input())

for _ in range(t):
    s1,s2,s3,s4 = [int(x) for x in input().split()]
    if max(s1,s2) < min(s3,s4) or min(s1,s2) > max(s3,s4):
        print("NO")
    else:
        print("YES")