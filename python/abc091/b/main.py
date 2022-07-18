#!/usr/bin/env python3

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    M = int(input())
    T = [input() for _ in range(M)]

    U = set(S+T+['_'])
    P = {}
    for u in U:
        P[u] = 0
    for i in range(M):
        P[u] = 0

    for s in U:
        for j in range(N):
            if s == S[j]:
                P[s] += 1
    for t in U:
        for j in range(M):
            if t == T[j]:
                P[t] -= 1
    print(max(P.values()))

main()
