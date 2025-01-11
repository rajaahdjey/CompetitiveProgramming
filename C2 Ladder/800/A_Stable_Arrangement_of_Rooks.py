t = int(input())

for _ in range(t):
    n , k = [int(x) for x in input().split()]

    ans = [["."]*n for _ in range(n)]

    last_row = 0
    while k > 0 and last_row < n:
        for i in range(n):
            for j in range(n):
                if i == last_row and j == last_row and k>0:
                    ans [i] [j] = 'R'
                    last_row += 2
                    k -= 1
                else:
                    continue

    if k <= 0:
        for row in ans:
            print("".join(row))
    else:
        print(-1)