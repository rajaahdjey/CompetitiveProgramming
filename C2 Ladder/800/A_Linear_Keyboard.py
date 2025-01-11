t = int(input())

for _ in range(t):
    keyboard = input()
    keyboard_dict = {x:i+1 for i,x in enumerate(keyboard)}
    s = input()
    ans = 0
    start = keyboard_dict[s[0]]
    for char in s[1:]:
        ans += abs(start-keyboard_dict[char])
        start = keyboard_dict[char]

    print(ans)



    
    