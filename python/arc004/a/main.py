#!/usr/bin/env python3

def main():
    def func(s):
        return list(map(int,s.split()))
    N = int(input()) 
    # P = [ func(input()) for _ in range(N)]
    P =  list(map(lambda s: list(map(int,s.split())),[input() for _ in range(N)] )) 
    
    
    print(P)

   
main()
