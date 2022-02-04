#https://www.acmicpc.net/problem/1929

def pn(n,m) :
    if n==1 : start=2
    else : start=n
    end=m
    for i in range(start,end) :
        cks=1
        for j in range(2,i) :
            if j*j<=end :
                if i%j==0 : cks=0
                else : pass
        if cks==1 : print(i)
    return 0
                
    
_n, _m=map(int, input().split())
pn_ls=pn(_n,_m)
#print(pn_ls)
