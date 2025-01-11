n , q = [int(x) for x in input().split()]

s = input()

ans_map = [0] * (n+1)

for i,char in enumerate(s):
    ans_map[i+1] = ans_map[i] + (ord(char)-96)

for _ in range(q):
    l , r = [int(x) for x in input().split()]
    print(ans_map[r]-ans_map[l-1])
