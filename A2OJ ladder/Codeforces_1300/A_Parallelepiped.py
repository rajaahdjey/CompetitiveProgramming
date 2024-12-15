s1,s2,s3 = [int(x) for x in input().split(" ")]

a = (s1*s2/s3)**0.5
b = (s2*s3/s1)**0.5
c = (s3*s1/s2)**0.5


print(int(4*(a+b+c)))