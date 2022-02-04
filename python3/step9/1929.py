#https://www.acmicpc.net/problem/1929

def pn(n,m) :
    start=n
    end=m

    a = [False,False] + [True]*(end-1)
    #print(a)
    primes=[]
    for i in range(2,end+1):
      if a[i]:
        if i>=start :
            primes.append(i)
        for j in range(2*i, end+1, i):
            a[j] = False

    return primes
                
    
_n, _m=map(int, input().split())
pn_ls=pn(_n,_m)

for i in pn_ls :
    print(i)
