#https://www.acmicpc.net/problem/1011

def lightyear(x,y) :
    dist=y-x
    t1,t2=1,2
    if dist==1 : return 1
    elif dist==2 : return 2
    else :
        group=1
        while True :
            ls=[]
            ls=[k for k in range(4, (2+2*group)+1, 2) ]
            #print(ls)
            group_last_n=sum(ls)+2
            if dist<= group_last_n  :
                #print(group)
                #print(group_last_n)
                break
            else :
                group+=1
                
    for i in range(0, group) :
        t1+=2
        t2+=2
    if group_last_n-(group+1)<dist : return t2
    else : return t1
        


    

n=int(input())
result=[]
for i in range(0,n) :
    a,b=map(int, input().split())
    result.append(lightyear(a,b))
    
for j in range(0,n) :
    print(result[j])
