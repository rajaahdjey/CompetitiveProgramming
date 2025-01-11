t = int(input())

for _ in range(t):
    s = input()
    a,b,c = 0,0,0
    for char in s:
        if char == 'A':
            a += 1
        elif char == 'B':
            b += 1
        else:
            c += 1
    if b == (a+c):
        print("YES")
    else:
        print("NO")