#!/usr/bin/env python3

def main():
    S = input()
    flag = False 

    for i in range(3):
        nums = 0
        for j in range(3):
            if i == j:
                continue
            if S[i] == S[j]:
                nums += 1
        if nums == 0:
            flag = True
            break
    
    if flag:
        print(S[i])
    else:
        print(-1)

main()
