#!/usr/bin/env python3

def main():
    S = input()
    T = input()
    
    lst = []
    j = 0
    flag = False

    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            lst.append(i)


    # print(lst)
    

    if T == S:
        flag = True
    
    while len(lst) > 0 and j+len(S) <= len(T):
        for i in lst:
            S_ = S[:i] + j * S[i] + S[i:]
            # print(S_)
            if T == S_:
                flag = True
                break

        j += 1

    
    if flag:
        print('Yes')
    else:
        print('No')

main()
