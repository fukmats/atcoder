#!/usr/bin/env python3
import numpy as np

def main():
    
    C = np.array([list(map(int, input().split())) for _ in range(3)])
    D = np.zeros_like(C)
    


    for a1 in range(C[0].min()+1):
        for a2 in range(C[1].min()+1):
            for a3 in range(C[2].min()+1):
                
                b1 = C[0][0] - a1
                b2 = C[1][1] - a2
                b3 = C[2][2] - a3
                a = [a1,a2,a3]
                b = [b1,b2,b3]

                flag = True

                for i in range(3):
                    for j in range(3):
                        if C[i][j] != a[i] + b[j]:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    break
            if flag:
                break  
        if flag:
            break
    if flag:
        print('Yes')
    else:
        print('No')


main()
