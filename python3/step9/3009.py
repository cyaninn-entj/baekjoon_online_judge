#https://www.acmicpc.net/problem/3009

x,y=0,0
x_ls=[]
y_ls=[]
for i in range(0,3) :
    x,y=map(int,input().split())
    x_ls.append(x)
    y_ls.append(y)

for i in range(0,3) :
    n1=x_ls[i]
    n2=y_ls[i]
    if x_ls.count(n1)==1 :
        _x=n1
    if y_ls.count(n2)==1 :
        _y=n2
        
print(_x,_y)
