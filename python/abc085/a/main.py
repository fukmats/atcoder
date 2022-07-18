#!/usr/bin/env python3

def main():
    N = int(input())
    D = [int(input()) for _ in range(N)]
    D = list(set(D))
    print(len(D))


main()
