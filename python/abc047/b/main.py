#!/usr/bin/env python3

def main():
    W,H,N = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    # print(A)

    x_max = W
    x_min = 0
    y_max = H
    y_min = 0
    for i in range(N):
        a = A[i][2]
        if a == 1:
            x_min = max(x_min,A[i][0])
        elif a == 2:
            x_max = min(x_max, A[i][0])
        elif a == 3:
            y_min = max(y_min,A[i][1])
        elif a == 4:
            y_max = min(y_max,A[i][1])
    
    if x_max > x_min and y_max > y_min:
        S = (x_max - x_min) * (y_max - y_min)
    else:
        S = 0
    print(S)

main()
