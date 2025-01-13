N , L = [int(x) for x in input().split()]

ans = [input() for _ in range(N)]

ans.sort()

print("".join(ans))