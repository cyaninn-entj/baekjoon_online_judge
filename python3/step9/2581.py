#https://www.acmicpc.net/problem/2581

def pn(num) :
    f=0
    if num==1 : return f
    for j in range(2,num) :
        if j*j<=num :
            if num%j==0 : return f
    return num


_m=int(input())
_n=int(input())
ls=[]

for i in range(_m,_n+1) :
    ls.append(pn(i))

#print(ls)
for k in ls[:] :
    if k==0 :
        ls.remove(0)

#print(ls)

if sum(ls)>0 :
    print(sum(ls))
    print(ls[0])
else : 
    print(-1)
