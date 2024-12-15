import math
count , pos = [int(x) for x  in input().split(" ")]

mid_point = math.ceil(count/2)

if pos <= mid_point:
    print((2*pos)-1)
else:
    #the number has to be even
    print((pos-mid_point)*2)