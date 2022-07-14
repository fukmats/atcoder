#!/usr/bin/env python3



def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))

    # st = time.time()
    dp = [float('inf') for _ in range(N)]
    # en = time.time()
    # print(en-st)
    
    def ch_min(dp, i, b):
        if dp[i] > b:
            dp[i] = b
            return True
        else:
            return False
    dp[0] = 0
    # st = time.time()
    # print(en-st)
    for i in range(1, N, 1):
        for k in range(0,K,1): 
            if i >= k: 
                ch_min(dp, i, abs(h[i] - h[i-(k+1)]) + dp[i-(k+1)])
        # en = time.time()
        # print(en-st)
    print(dp[-1])


# N = 10**5
# K = 100
# h = [10**4 for _ in range(10**5) ]
# main(N,K,h)
main()