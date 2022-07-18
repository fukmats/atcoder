#!/usr/bin/env python3
import math

def main():
    A,B,C,X,Y = map(int, input().split())

    
    tmin = float('inf')
    
    # for i in range(X+1):
    #     for j in range(Y+1):
    #         a = i
    #         b = j
    #         c = max(2*(X-i),2*(Y-j))
    #         t = a * A + b * B + c * C
    #         tmin = min(tmin,t)
    # print(tmin)

    for c in range(2*max(X,Y)+1):
        a = X - math.floor(c/2)
        b = Y - math.floor(c/2)
        if a < 0:
            a = 0
        if b < 0:
            b = 0
        t = a * A + b * B + c * C
        tmin = min(tmin,t)
        if t == 7600:
            print(a,b,c)
    print(tmin)


main()
