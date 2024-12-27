s = input()

required = "hello"

match_w=  ""

pos = 0
for letter in required:
    while pos < len(s):
        if letter == s[pos]:
            match_w += s[pos]
            # print(match_w)
            pos += 1
            break
        pos += 1




if match_w == "hello":
    print("YES")
else:
    print("NO")