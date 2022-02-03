#https://www.acmicpc.net/problem/2775

def hmp(f,n) :
    floor=f
    num=n
    floor_ls=[x for x in range(1,num+1)]
    for i in range(floor):
        for j in range(1, num):
            floor_ls[j] += floor_ls[j-1]
        #print(floor_ls)  # 프린트문을 추가
    
    return (floor_ls[num-1])


_t=int(input())
val=[]
for j in range(0,_t) :
    f=int(input())
    n=int(input())
    val.append(hmp(f,n))
    
for l in range(0,_t) :
    print(val[l])
