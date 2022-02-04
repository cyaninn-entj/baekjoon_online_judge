#https://www.acmicpc.net/problem/1929

def pn(n,m) :
    start=n
    end=m
    no_odd=[]
    for i in range(start,end) :
        cks=1
        for j in range(2,i) :
            if j*j<=end :
                if i%j==0 : cks=0
                else : pass
        if cks==1 : no_odd.append(i)
    return no_odd
                
    
_n, _m=map(int, input().split())

pn_ls=pn(_n,_m)
#print(pn_ls)

for i in range(len(pn_ls)) :
    print(pn_ls[i])
