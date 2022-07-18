#!/usr/bin/env python3

def main():
    N,L = map(int, input().split())
    S = [input() for _ in range(N)]

    S.sort()
    print(''.join(S))
    


main()