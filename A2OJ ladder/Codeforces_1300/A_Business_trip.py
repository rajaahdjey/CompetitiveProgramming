k_needed = int(input())

monthly_growth = [int(x) for x in input().split(" ")]

monthly_growth.sort(reverse=True)

ctr = 0
k_grown = 0

for i in monthly_growth:
    if k_grown < k_needed:
        k_grown += i
        ctr += 1
    else:
        break

if k_grown >= k_needed:
    print(ctr)
else:
    print(-1)