#!/usr/bin/env python3
from cmath import inf
import random

def main():
    min_cost = []
    def ch_min(min_cost, i, b):
        if min_cost[i] >= b:
            min_cost[i] = b
            return True
        else:
            return False

    N = int(input())
    h = list(map(lambda h: int(h), input().split()))

    min_cost = [inf for _ in range(N)]
    for i in range(N):
        if i == 0:
            min_cost[i] = 0
            # print(min_cost)
            continue
        if i == 1:
            min_cost[i] = abs(h[i]-h[i-1])
            # print(abs(h[i]-h[i-1]))
            continue
        ch_min(min_cost, i, abs(h[i]-h[i-1])+min_cost[i-1])
        ch_min(min_cost, i, abs(h[i]-h[i-2])+min_cost[i-2])
    # print(min_cost[-5:])
    print(min_cost[N-1])



# h_test = [[1,1], [1,10000], [10000,1], [10000,10000], [10000 for _ in range(100000)]]

# for h in h_test:
#     main(len(h), h)


main()
