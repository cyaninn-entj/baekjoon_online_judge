#https://www.acmicpc.net/problem/4153

while True : 
    t_ls=[]
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0 :
        break
    t_ls.append(a); t_ls.append(b); t_ls.append(c)
    
    c=max(t_ls)
    t_ls.remove(max(t_ls))
    #print(c,t_ls)
    
    if c**2 == (t_ls[0]**2) + (t_ls[1]**2) :
        print('right')
    else : 
        print('wrong')
