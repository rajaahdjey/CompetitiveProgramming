for _ in range(int(input())):
    n = int(input())
    ct = 0
    for i in range(1,10):
        num = 0
        for j in range(0,10):
            num = num*10+i
            if num <= n:
                ct += 1

    print(ct)
