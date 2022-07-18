#!/usr/bin/env python3

def main():
    import numpy as np
    from math import sin, cos, radians
    a,b,d = map(int, input().split())

    A = np.array([a,b])
    t = radians(-d)
    D = np.array([[cos(t), -sin(t)],[sin(t), cos(t)]])
    ans = np.dot(A,D)
    print(f'{ans[0]} {ans[1]}')

main()
