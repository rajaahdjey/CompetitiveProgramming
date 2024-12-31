t = int(input())

for _ in range(t):
    n = int(input())
    new_pos = []
    if n % 2 == 0:
        for i in range(1,n+1):
            if i % 2 == 0:
                new_pos.append(i-1)
            else:
                new_pos.append(i+1)
    else:
        new_pos = [3,1,2]
        for i in range(4,n+1):
            if i % 2 == 0:
                new_pos.append(i+1)
            else:
                new_pos.append(i-1)
    
    print(*new_pos)
