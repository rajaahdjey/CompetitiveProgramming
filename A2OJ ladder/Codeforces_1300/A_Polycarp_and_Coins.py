t = int(input())

#c1 + 2c2 = n3
#c1 + 2c1 = n3
#c1 = n3//3

#c1 - c2 = 0


for _ in range(t):
    n = int(input())
    c1 = (n // 3)
    c2 = (n-c1)//2
    c1 = n - 2*c2
    print(c1,c2)


#Better soln 
#ideally , c1 = c2 = n//3 
#if no remainders, c1 = c2
#if remainder = 1 , c1 += 1
#if remainder = 2, c2 += 1
# 
 