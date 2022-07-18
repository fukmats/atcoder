#!/usr/bin/env python3

def main():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    S = set(A)
    if len(S) <= K:
        ans = 0
    else:
        D = {}
        for s in S:
            D[s] = 0
        for i in range(N):
            D[A[i]] += 1

        B = []
        for k in D.keys():
            B.append([k,D[k]])
        B.sort(key=lambda x: x[1])

        ans = sum(list(map(lambda x: x[1],B[:len(B)-K])))
    print(ans)









main()