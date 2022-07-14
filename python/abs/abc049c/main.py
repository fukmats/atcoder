#!/usr/bin/env python3

def main():
    N = 10 ** 5

    S = input()
    def ch_eq(dp, i, b):
        if dp[i-1] + b == S:
            dp[i] = b
            return True
        else:
            return False

    s_list = [
        'dreamer',
        'dream',
        'eraser',
        'erase'
    ]
    dp = []
    for i in range(N):
        for s in s_list:
            flag = ch_eq(dp,i,s)


    




    if S_ == '' or S__ == '':
        print('YES')

    else:
        print('NO')


main()
