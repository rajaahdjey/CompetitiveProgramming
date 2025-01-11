t = int(input())

for _ in range(t):
    n , k = [int(x) for x in input().split()]
    a_arr = [int(x) for x in input().split()]
    b_arr = [int(x) for x in input().split()]

    comb_tup = tuple(zip(a_arr,b_arr))

    comb_tup = sorted(comb_tup)

    for (a,b) in comb_tup:
        if a <= k:
            k += b

    print(k)
