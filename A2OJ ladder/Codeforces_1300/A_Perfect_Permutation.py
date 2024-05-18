perm_size = int(input())

#permutation needs to follow 2 rules :

#1. Element i cannot be at position i 
#2. Element i must obey rule p [ p[i]] == i

#Example : 
# n = 2 --> elements are 1 , 2 
# p[p[i]] == 1

#so we need to answer in such a way that p[p[1]] == 1 and p[p[2]] == 2 
# if p1 = 2 and p2 = 1, this can be satisfied. --> p[2] = 1 annd p[1] == 2 --> this would only happen when elements are directly swapped with one another

# n = 3 --> elements are 1 , 2 , 3 
# pos pi = i

#so pos_p1 = 1 , pos_p2 = 2 , pos_p3 = 3 
#if p1 = 3 , p2 = 1 , p3 = 2 --> can this be satisfied? 


if perm_size % 2 != 0 :
    print(-1)
else:
    i = 1
    final_list = ""
    while i <= perm_size:
        if i % 2 == 0:
            final_list += str(i)
            final_list += " "
            final_list += str(i-1)
            final_list += " "
            i += 2
        else:
            i += 1
            continue
    print(final_list)
