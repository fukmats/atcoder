#!/usr/bin/env python3
import numpy as np

# def main():
#     N = int(input())
#     A = [list(map(int, input().split())) for _ in range(N)]

#     hmin = np.array(A)[:,2].max()
#     for h in range(hmin, 10**9+1):
#         for cx in range(101):
#             for cy in range(101):
            
#                 # print(cx,cy,h)
#                 flag = True
#                 for i in range(N):
#                     if max(h - abs(A[i][0]-cx) - abs(A[i][1]-cy),0) != A[i][2]:
#                         flag = False
#                         break
#                 # flag = True
#                 if flag:
#                     break
#             if flag:
#                 break
#         if flag:
#             break
#     if flag:
#         print(f'{cx} {cy} {h}')


# main()

#!/usr/bin/env python3
import numpy as np

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
       
    for cx in range(101):
        for cy in range(101):
            for i in range(N):
                if A[i][2] > 0:
                    H = A[i][2] + abs(A[i][0]-cx) + abs(A[i][1]-cy)
                    break
            flag = True
            for i in range(N):
                if max(H - abs(A[i][0]-cx) - abs(A[i][1]-cy),0) != A[i][2]:
                    flag = False
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        print(f'{cx} {cy} {H}')
     


main()
