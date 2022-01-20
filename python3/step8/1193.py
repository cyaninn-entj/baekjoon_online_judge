#https://www.acmicpc.net/problem/1193


def findgroup(N) :
    g_last_num=1
    n=1
    Gnum=1
    userIN=N
    while True :
        if userIN==1 :
            Gnum=1
            An=1
            break;
        elif userIN <= g_last_num :
            Gnum=n
            break;
        else :
            n+=1
            g_last_num+=n
    return Gnum,g_last_num

nm,dm=0,0
NO=int(input())
G_num, G_last_num=findgroup(NO)
#print(G_num, G_last_num)

if G_num%2==1 :
    dm=G_num-(G_last_num-NO)
    nm=1+(G_last_num-NO)
else :
    dm=1+(G_last_num-NO)
    nm=G_num-(G_last_num-NO)
    
print(str(nm)+"/"+str(dm))
