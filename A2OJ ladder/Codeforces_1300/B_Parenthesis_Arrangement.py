n_costa_costb = [int(x) for x in input().split(" ")]
string = input()

cost = 0
i = 0
j = 0
count_open = 0
count_close = 0
count_match = 0
count_double = 0
while i < 2 * n_costa_costb[0]:
    if string[i] == "(":
        count_open += 1
    else:
        count_close += 1
    i = i + 1

Flag = False
while j < 2 * n_costa_costb[0]:
    if string[j] == "(" and string[j + 1] == ")":
        j += 2
        count_match += 2
    elif (string[j] == "(" and string[j + 1] == "(") or (string[j] == ")" and string[j + 1] == ")"):
        if ((string[j] == ")" and string[j + 1] == ")")) and Flag == False :
            Flag = True
        elif ((string[j] == ")" and string[j + 1] == ")")) and Flag ==True :
            Flag = False
            count_double += 4
        elif ((string[j] == "(" and string[j + 1] == "(")) and Flag == True :
            Flag = True
        else  :
            Flag = True
            
        j += 2
        
    else:
        j += 2



cost = ((n_costa_costb[0]*2 - count_match - abs(count_open-count_close)-count_double)*(n_costa_costb[1]) / 2 ) + (abs(count_close-count_open)*n_costa_costb[2]/2 )



# print((n_costa_costb[0]*2 - count_match - abs(count_open-count_close))*(n_costa_costb[1]) / 2)
# print((abs(count_close-count_open)*n_costa_costb[2]/2 ) )
# print((count_double-abs(count_open-count_close))*(n_costa_costb[1]) / 2 )
print(2*n_costa_costb[0])
# print(count_close)
# print(count_open)
print(count_match)
print(count_double)
print( abs(count_open-count_close))
print(int(cost))

# print((n_costa_costb[0]*2 - count_match - abs(count_open-count_close)))

# print(int(cost))