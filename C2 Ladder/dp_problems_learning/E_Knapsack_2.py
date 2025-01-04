N , W = [int(x) for x in input().split()]

weights = []
values = []

for i in range(0,N):
    w , v = [int(x) for x in input().split()]
    weights.append(w)
    values.append(v)
total_sum = sum(values)
# print("Total sum:",total_sum)
ans = [float("inf")]*(total_sum+1)
ans[0] = 0
# print(values)
# print(len(ans))
for i in range(0,N):
    item_weight = weights[i]
    item_value = values[i]
    for j in range(total_sum,item_value-1,-1):
        # print(j,item_value,item_weight,ans[j])
        ans[j] = min(ans[j], (ans[j - item_value]+item_weight))

result = 0
for val in range(total_sum+1):
    if ans[val] <= W:
        result = val

print(result)