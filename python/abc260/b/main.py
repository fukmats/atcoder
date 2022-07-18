#!/usr/bin/env python3

def main():
    N,X,Y,Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append([i+1,A[i],B[i],A[i]+B[i]])

    C.sort(key=lambda x: x[0])
    C.sort(key=lambda x: x[1], reverse=True)
    
    ans = C[:X]
    C = C[X:]

    C.sort(key=lambda x: x[0])
    C.sort(key=lambda x: x[2], reverse=True)
    ans += C[:Y]
    C = C[Y:]

    C.sort(key=lambda x: x[0])
    C.sort(key=lambda x: x[3], reverse=True)
    ans += C[:Z]

    ans.sort(key=lambda x: x[0])

    for j in range(len(ans)):
        print(ans[j][0])



    


main()
