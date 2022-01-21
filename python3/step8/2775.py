#https://www.acmicpc.net/problem/2775

def hmp(k,n) :
    floor=k
    num=n
    floor_ls=[]
    _sum=0
    if floor>1 :
        for i in range(1, n+1) :
            floor_ls.append( hmp(floor-1,i) )
    else : 
        for i in range(1, n+1) :
            _sum+=i
        return _sum
    result=sum(floor_ls)
    #print(floor_ls)
    return result


_t=int(input())
val=[]
for j in range(0,_t) :
    k=int(input())
    n=int(input())
    val.append(hmp(k,n))
    
for l in range(0,_t) :
    print(val[l])
