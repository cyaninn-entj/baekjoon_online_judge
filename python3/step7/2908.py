#https://www.acmicpc.net/problem/2908
def rev_num(num) :
    t=str(num)
    result=0
    
    result=int(t[0])
    result+=int(t[1])*10
    result+=int(t[2])*100
    return result

a,b=input().split()
rev_a=rev_num(a)
rev_b=rev_num(b)

if rev_a > rev_b : 
    print(rev_a)
else : 
    print(rev_b)
