#!/usr/bin/env python3
import numpy as np




def main():
    N,X,Y = map(int, input().split())
    def red(R,B,n):
        R[n-1],B[n],R[n] = R[n-1]+R[n],B[n]+X*R[n],0
        # print(R,B)
        return R,B
    
    def blue(R,B,n):
        R[n-1],B[n-1],B[n] = R[n-1]+B[n],B[n-1]+Y*B[n],0
        # print(R,B)
        return R,B

    R = {}
    B = {}
    for i in range(1,N+1):
        R[i] = 0
        B[i] = 0

    R[N] = 1
    for i in reversed(range(2,N+1)):
        R,B = red(R,B,i)
        R,B = blue(R,B,i)
        # print(R,B)
        # break
    print(B[1])

main()
