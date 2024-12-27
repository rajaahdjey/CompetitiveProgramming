n = int(input())

#--0--
#-010-
#01210
#-010-
#--0--

#num characters per row = 

chars_per_row = (n*2)+1

for i in range(0,n+1):
    s = ""
    for j in range(0,i+1):
        s += str(j) + " "
    for k in range(i-1,-1,-1):
        s = s+str(k) + " "
    print((" "*(n-i)*2 + s).rstrip())

for i in range(n-1,-1,-1):
    s = ""
    for j in range(0,i+1):
        s += str(j) + " "
    for k in range(i-1,-1,-1):
        s = s+str(k) + " "
    print((" "*(n-i)*2 + s).rstrip())


