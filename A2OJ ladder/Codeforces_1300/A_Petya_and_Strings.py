import string
string_1 = input()
string_2 = input()

nos = [x for x in range(1,27)]
chars = list(string.ascii_lowercase)

lookup = dict(zip(chars,nos))

same_flag = True
for i,_ in enumerate(string_1):
    if (lookup[string_1[i].lower()] - lookup[string_2[i].lower()]) > 0:
        print(1)
        same_flag = False
        break
    elif (lookup[string_1[i].lower()] - lookup[string_2[i].lower()]) < 0:
        print(-1)
        same_flag = False
        break

if same_flag:
    print(0)