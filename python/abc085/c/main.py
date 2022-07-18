#!/usr/bin/env python3

def main():
    N, Y = map(int, input().split())

    ans = [-1,-1,-1]
    flag = False
    t = 0


    for i in range(0,N+1):
        if i * 10000 > Y:
            break
        for j in range(0,N-i+1):  
            t = 10000 * i + 5000 * j + 1000 * (N-i-j)
            if t == Y:
                flag = True
                ans = [i, j, N-i-j]
                break
        if flag:
            break
    

    print(f'{ans[0]} {ans[1]} {ans[2]}') 

main()
