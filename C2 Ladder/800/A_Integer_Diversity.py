t = int(input())

for _ in range(t):
    n = int(input())
    zeros = 0
    all_nos = set()
    abs_nos = set()
    for x in input().split():
        if int(x) == 0:
            zeros += 1
        else:
            all_nos.add(int(x))
            abs_nos.add(abs(int(x)))
    print(abs_nos)
    print(all_nos)
    print(zeros)
    if zeros > 0:
        print(len(abs_nos)+(len(all_nos)-len(abs_nos))+1)
    else:
        print(len(abs_nos)+(len(all_nos)-len(abs_nos)))
