import sys

input = sys.stdin.read

data = input().splitlines()

n = int(data[0])

points = []

for i in range(1, n+1):
    x,y = map(int, data[i].split())
    points.append((x,y))

supercentral = 0

for (x,y) in points:
    # print(f"Checking ({x},{y})")
    right_surround = False
    left_surround = False
    top_surround = False
    bottom_surround = False
    for (x1,y1) in points:
        # print(f"Checking with ({x1},{y1})")
        if (x == x1) & (y < y1):
            top_surround = True
            # print(f"({x},{y}) top surrounded by {x1},{y1}")
        if (x == x1) & (y > y1):
            bottom_surround = True
            # print(f"({x},{y}) bot surrounded by {x1},{y1}")
        if (x < x1) & (y == y1):
            right_surround = True
            # print(f"({x},{y}) right surrounded by {x1},{y1}")
        if (x > x1) & (y == y1):
            left_surround = True
            # print(f"({x},{y}) left surrounded by {x1},{y1}")

    supercentral += int(right_surround*left_surround*top_surround*bottom_surround)

print(supercentral)