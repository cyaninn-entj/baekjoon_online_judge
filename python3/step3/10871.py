#https://www.acmicpc.net/problem/10871
N, X = map(int, input().split())

A_ls=list( map(int, input().split()) )

for i in range(0,N) : 
    if A_ls[i]<X :
        print("%d " % A_ls[i],end="")

