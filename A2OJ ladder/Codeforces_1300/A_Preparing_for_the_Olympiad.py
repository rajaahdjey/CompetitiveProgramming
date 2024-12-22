t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    b = [int(x) for x in input().split(" ")]

    a_score = 0
    b_score = 0

    for i in range(n):
        if i != n-1:
            if (a[i]-b[i+1]) > 0:
                a_score += a[i]
                b_score += b[i+1]
        else:
            a_score += a[i]

    print(a_score-b_score)

