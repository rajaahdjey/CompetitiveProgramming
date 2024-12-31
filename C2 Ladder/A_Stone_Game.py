t = int(input())


for _ in range(t):
    n = int(input())
    power = [int(x) for x in input().split()]
    pos_min = None
    pos_max = None
    for i in range(n):
        if power[i] == 1:
            pos_min = i+1
        if power[i] == n:
            pos_max = i+1
    first_pos = min(pos_min,pos_max)
    last_pos = max(pos_min,pos_max)
    print(min(last_pos , n+1 - first_pos, first_pos + n+1 - last_pos))