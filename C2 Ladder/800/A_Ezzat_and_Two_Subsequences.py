for _ in range(int(input())):
    n = int(input())
    a_list = [int(x) for x in input().split()]
    a_list.sort()
    s_array_a = a_list[-1]
    s_array_b = a_list[:-1]
    print(s_array_a+sum(s_array_b)/len(s_array_b))


#make it better 
#instead of sorting entire array , just get the max value ... array 1 is max value , 
#array 2 is sum of total array minus max val 
