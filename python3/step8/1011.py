#https://www.acmicpc.net/problem/1011

def lightyear(x,y) :
    pos=x+1
    time=1
    dist=1
    
    while True :
        if pos < y-1 :
            pass
        elif pos==y-1 :
            time+=1
            break;
        elif pos >= y :
            time+=1
            break;
        dist+=1
        pos+=dist
        time+=1
    return time
        

    
    
n=int(input())
result=[]
for i in range(0,n) :
    a,b=map(int, input().split())
    result.append(lightyear(a,b))
    
for j in range(0,n) :
    print(result[j])
