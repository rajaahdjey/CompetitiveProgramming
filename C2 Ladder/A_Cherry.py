t = int(input())

for _ in range(t):
    n = int(input())
    all_nos = [int(x) for x in input().split()]
    prod = 0
    for i in range(0,n-1):
            if all_nos[i]*all_nos[i+1] > prod:
                prod = all_nos[i]*all_nos[i+1]

    print(prod)

