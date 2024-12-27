n,a,b = [int(x) for x in input().split(" ")]

#no less than a people in front ---> atleast (n-a)
#no more than b people behind ---> atmost (n-b)

#if x is possible positions, 
# #123456789

# #1234_____

print(min (n-a,b+1))