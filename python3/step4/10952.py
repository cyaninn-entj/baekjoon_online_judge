#https://www.acmicpc.net/problem/10952

a=[]
b=[]

i=0
while True :
    a_in, b_in = map(int, input().split())
    a.append(a_in)
    b.append(b_in)

    i=i+1

    if a_in==b_in==0 :
        break

for i in range(0,len(a)-1) :
    print(a[i]+b[i])
