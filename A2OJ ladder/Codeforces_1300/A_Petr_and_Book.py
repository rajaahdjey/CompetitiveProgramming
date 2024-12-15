import sys

input = sys.stdin.read

data = input().splitlines()

n = int(data[0])

# mon,tues,wed,thurs,fri,sat,sun = map(int, data[1].split(" "))

while n > 0:
    for i,pages in enumerate(data[1].split(" ")):
        # print(f"{i+1} day with {n} pages remaining and {pages} pages to be read")
        n -= int(pages)
        if n <= 0:
            break

print(i+1)

