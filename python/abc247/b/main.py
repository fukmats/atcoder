#!/usr/bin/env python3

def main():
    N = int(input())
    name_list = {}
    s = []
    t = []
    for i in range(N):
        s_,t_ = input().split()
        s.append(s_)
        t.append(t_)

    def z(a, s, t, i, x):
        flag = False
        a.append(x)
        # print(i,a)
        for i_ in range(N):
            for j_ in range(i+1):
                if i_ == j_:
                    continue
                if s[i_] == a[j_] or t[i_] == a[j_]:
                    a.pop()
                    return False
        return True

    a = []
    for i in range(N):
        flag = z(a, s, t, i, s[i])
        if flag == False:
            flag = z(a,s,t,i,t[i])
        if flag == False:
            break
    if flag:
        print('Yes')
    else:
        print('No')





main()
