#!/usr/bin/env python3

def main():

    N,M,X,T,D = map(int, input().split())

    t = [0] * (N+1)
    t[0] = T - D * X
    for i in range(1,X+1):
        t[i] = t[i-1] + D
    for i in range(X+1,N+1):
        t[i] = t[i-1]
    print(t[M])




main()
