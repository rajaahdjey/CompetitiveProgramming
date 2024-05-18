seq = [int(x) for x in input().split(" ")]

#logic would be as follows 
#we have n .... m
#we need to check that m is the immediate next prime after n
#this will only be true if there are no prime numbers in between n and m AND m needs to be prime.

#so logic will be as follows
#start with x = n+ 1 and loop until m
#for i in range(2,x)
#if i is divisible by any of these nos, x is not prime. continue with x+1
#if i is not divisible by any of these nos, check if the x is equal to m.
#return YES only if x is not divisible by any of these nos and x is equal to m
#else return no.

j = seq[0]+1 #start with one number after the first number
flag = True
while j <= seq[1] and flag:
    i = 2 
    # print(i,j)
    while i < j and flag:
        # print(i,j)
        if j % i == 0:
            if j == seq[1]:
                print("NO")
            j += 1
            i = 2 #re-initialize i to 2 , otherwise it will only check from latest i for new j. 
        if j-1 == i: #end of check
            if j == seq[1]:
                #j is equal to m
                print("YES")
                flag = False
            else:
                print("NO")
                flag = False
        if j > seq[1]:
            break
        i += 1
    j += 1
    
            
    
    

