instructions = input()

flag=False
for comm in instructions:
    if comm in {'H','Q','9'}: #ignore + as it doesnt produce output
        print("YES")
        flag = True
        break
if not(flag):
    print("NO")