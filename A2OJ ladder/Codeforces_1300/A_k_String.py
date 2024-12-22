k = int(input())
s = input()

s_dict = {}

for letter in s:
    if letter in s_dict:
        s_dict[letter] += 1
    else:
        s_dict[letter] = 1

final_string= ""

for letter in s_dict:
    if s_dict[letter] % k != 0:
        final_string = None
        break
    else:
        final_string += letter*int(s_dict[letter]/k)

if final_string is not None:
    print(final_string*k)
else:
    print(-1)