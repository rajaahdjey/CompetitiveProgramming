#bad solution

# t = int(input())

# for _ in range(t):
#     s = input()
#     flag = "NO"
#     start_ord = 97
#     L , R = 0 , 0
#     for i in range(len(s)):
#         if ord(s[i])-97 == 0:
#             flag = "YES"
#             L = i-1
#             R = i+1
#             break

#     if flag == "YES":
#         next_char = start_ord + 1
#         while L>=0 or R<len(s):
#             if L >=0 and ord(s[L]) == next_char:
#                 L -= 1
#                 next_char = next_char + 1
#                 continue
#             elif R < len(s) and ord(s[R]) == next_char:
#                 R += 1
#                 next_char = next_char + 1
#                 continue
#             else:
#                 flag = "NO"
#                 break
            
    
#     print(flag)
                


#better solution 

t = int(input())
for _ in range(t):
    s = input()
    L , R = 0 , len(s)-1
    last_char = 97+R #a is 96
    flag= "YES"
    for i in range(last_char,96,-1):
        if ord(s[L]) == i:
            L += 1
        elif ord(s[R]) == i:
            R -= 1
        else:
            flag = "NO"
            break
    print(flag)



