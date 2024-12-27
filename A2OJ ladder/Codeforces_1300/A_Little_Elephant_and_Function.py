n = int(input())

series = []

if n == 1:
    series = [1]
else:
    for i in range(1,n+1):
        if i != 1:
            series.append(i-1)
        else:
            series.append(n)

print(*series)


#working
# x = 2 ... 2 1 

# f(1) = swap (a0 and a1)

# # x = 3 ... 2 3 1 

# f(2) = swap (a1 and a2)  # 2 1 3
# f(1) = swap (a0 and a1)  # 1 2 3

# # x = 4 .. 2 3 4 1

# f(3) = swap (a2 and a3) # 2 3 1 4
# f(2) = swap (a1 and a2) # 2 1 3 4
# f(1) = swap (a0 and a1) # 1 2 3 4