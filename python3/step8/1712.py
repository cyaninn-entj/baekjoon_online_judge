#https://www.acmicpc.net/problem/1712

A,B,C=input().split()

perA=1
perB=int(B)/int(A)
perC=int(C)/int(A)

X=1
income=perC-perB
outlay=0

while True :
    if perB>=perC :
        X= -1
        break;
    outlay=perA/X
    #print(X, outlay, income)
    if outlay < income :
        break;
    X+=1

print(X)
