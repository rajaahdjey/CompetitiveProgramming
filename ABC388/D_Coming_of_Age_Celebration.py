N = int(input())

A = [int(x) for x in input().split()]

ans = [0]* (N)

sums = [0] * (N)
zeros = [0] * (N)
for i in range(N):
    print(sums)
    print(ans)
    print(zeros)
    print("**********")
    ans[i] = (N-1-i)
    sums[i] = A[i] + (i)
    if i > 0:
        zeros[i] += zeros[i-1]
    if (ans[i] - sums[i]) > 0:
        zeros[i + 1 + (sums[i])] += 1
        
final_ans = []

for i in range(N):
    solved = sums[i] - ans[i] - zeros[i]
    if solved >= 0:
        final_ans.append(solved)
    else:
        final_ans.append(0)

print(" ".join(map(str, final_ans)))