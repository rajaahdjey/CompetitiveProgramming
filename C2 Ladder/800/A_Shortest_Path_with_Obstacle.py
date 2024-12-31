t = int(input())

for _ in range(t):
    ignore = input()
    xa,ya = [int(x) for x in input().split()]
    xb,yb = [int(x) for x in input().split()]
    xf,yf = [int(x) for x in input().split()]

    x_dist_needed = xb-xa
    y_dist_needed = yb-ya

    num_steps = 0
    if (xa == xf) and (xb == xf) and (min(ya,yb) < yf < max(ya,yb)):
        num_steps += abs(xb-xa) + 2
    else:
        num_steps += abs(xb-xa)
    if (ya == yf) and (yb == yf) and (min(xa,xb) < xf < max(xa,xb)):
        num_steps += abs(yb-ya) + 2
    else:
        num_steps += abs(yb-ya)
    
    print(num_steps)



