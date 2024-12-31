t = int(input())

for _ in range(t):
    a,b,c = [int(x) for x in input().split()]
    tot_n = (max(a,b)-min(a,b))*2
    # print(tot_n)
    if a > tot_n or b > tot_n or c > tot_n:
        print(-1)
    else:
        if c <= tot_n//2:
            print((tot_n//2)+c)
        else:
            print(c-(tot_n//2))