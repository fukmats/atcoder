#!/usr/bin/env python3

def main():
    N,K = map(int, input().split())
    L = list(map(int, input().split()))

    L.sort(reverse=True)
    print(sum(L[:K]))

main()
