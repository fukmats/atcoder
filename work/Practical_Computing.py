import numpy as np
def main(n):
    # a = np.zeros((30,30))
    for i in range(n-1):
        print(i)
        l = i+1
        for j in range(i):
            if i == j:
                a[i][j] = 1
            else:
                a[i][j] = a[i-1][j-1] + a[i-1][j]
        print(a)

if __name__ == "__main__":
    # for n in range(5):
    n = 3
    main(n)