#https://www.acmicpc.net/problem/11653

def fz(num) :
    cks=0
    for i in pn_ls :
        v=int(num/i)
        if num%i==0 :
            ls.append(i)
            cks=1
            if v==1 :
                return ls
            else :
                fz(v); break
    if cks==0 :
        ls.append(num)
    return ls

pn_ls=[]
ls=[]
end=3162
a=[False,False]+[True]*(end+1)
for o in range(2,end) :
    if a[o] :
        pn_ls.append(o)
        for j in range(o*2,end,o) :
            a[j]=False

n=int(input())
if n==1 : pass
else :
    result=fz(n)
    for i in result :
        print(i)
        
#print(pn_ls[:1010])
#print(ls)
