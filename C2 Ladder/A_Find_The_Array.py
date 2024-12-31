import math
t = int(input())


for _ in range(t):
    s = int(input())

    #out minimum possible size of a beautiful array with the sum of elements equal to s.
    #beautiful if the following condition is held for every i from 1 to n: 
    #either ai=1, or at least one of the numbers ai−1 and ai−2 exists in the array as well.
    # ai - 1 , ai - 2 , ai = 1 
    # max_perfect series = 1 + (1+2) + (3+2) + ...  = n^2 , so we need atleast sqrt(s) to build s.

    print(math.ceil(math.sqrt(s)))

