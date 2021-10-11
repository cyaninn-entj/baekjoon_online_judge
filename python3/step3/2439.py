#https://www.acmicpc.net/problem/2439
n=int(input())

for i in range(0,n) :
    for k in range(n-(i+1),0,-1) :
        print(" ",end="")
    for j in range(0,i+1) :
        print("*",end="")
    print("")
