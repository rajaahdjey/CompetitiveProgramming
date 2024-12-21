N , D = [int(x) for x in input().split(" ")]
S = input()

cookies = 0
empty = 0

for box in S:
    if box == "@":
        cookies += 1
    else:
        empty += 1

print(empty+D)