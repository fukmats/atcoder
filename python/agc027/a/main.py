N,x = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
total = 0
G = [0] * N

for i in range(N):
    # print(G)
    # print(x)
    if x < A[i]:
        G[i] = x
        x = 0
    else:
        G[i] = A[i] 
        x -= A[i]
        total += 1
if total > 0 and x != 0:
    total -= 1
# sum(A == G)
print(total)


