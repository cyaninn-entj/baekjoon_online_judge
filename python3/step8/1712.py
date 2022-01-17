#https://www.acmicpc.net/problem/1712

A,B,C=input().split()

outlay, income=0,0
X=1
while True :
    if int(B)>=int(C) :
        X= -1
        break;
    outlay=int(A)+(int(B)*X)
    income=int(C)*X
    X+=1
    #print(X, outlay, income)
    if outlay <= income :
        break;
    
print(X)
