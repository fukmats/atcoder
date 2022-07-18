#!/usr/bin/env python3
import math

def main():
    
    N = int(input())

    def func(A,B):
        return max(math.ceil(math.log10(A+1)), math.ceil(math.log10(B+1)))
    vmin = float('inf')
    if N == 1:
        print(1)
    else:
        for i in range(1,math.ceil(math.sqrt(N))+1):
            if N % i != 0:
                continue
            vmin = min(vmin,func(i, N/i))

        print(vmin)


main()
