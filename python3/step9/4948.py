#https://www.acmicpc.net/problem/4948

def pn(num) :
    start=num+1
    end=2*num
    
    a = [False,False] + [True]*(end-1)
    #print(a)
    primes=[]
    for i in range(2,end+1):
      if a[i]:
        if i>=start :
            primes.append(i)
        for j in range(2*i, end+1, i):
            a[j] = False
    return len(primes)

def main() :
    n=int(input())
    if n==0 :
        return 0
    else :
        print(pn(n))
        return 1

while True :
    cks=main()
    if cks==0 :
        break
    else :
        pass
