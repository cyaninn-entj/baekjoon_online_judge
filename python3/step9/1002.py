#https://www.acmicpc.net/problem/1002

n=int(input())

for _ in range(n) :
    x1,y1,r1,x2,y2,r2=map(int, input().split())
    r_d=r1+r2
    #m_d=abs(x1-x2)+abs(y1-y2)
    m_d=abs(x1-x2)**2 + abs(y1-y2)**2
    #print(m_d)
    
    if r_d < m_d : 
        print(0)
    elif r_d==m_d : 
        if x1==x2 or y1==y2 :
            print(1)
        #else :
            #print(-1)
    else :
        if r1-r2==0 :
            print(0)
        elif r1-r2<0 :
            if m_d+r1 < r2 : print(0)
            elif m_d+r1==r2 : print(1)
            else : print(2)
        elif r1-r2>0 :
            if m_d+r2 < r1 : print(0)
            elif m_d+r2==r1 : print(1)
            else : print(2)
