t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    sorted_string = sorted(s)
    k = 0
    for i in range(n):
        if s[i] != sorted_string[i]:
            k += 1
    
    print(k)