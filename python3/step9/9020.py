#https://www.acmicpc.net/problem/9020

def pn(ad) :
    for i in range(2,ad) :
        if i*i<= ad :
            if ad%i==0 : return False
    return True
            
def GB_conjecture(idx) :
    x,y=int(idx/2), int(idx/2)
    while True : 
        _x=pn(x)
        _y=pn(y)
        if _x and _y :
            return x,y
        else :
            x-=1
            y+=1

    

n=int(input())
for run in range(n) :
    num=int(input())
    a,b= GB_conjecture(num)
    print(a,b)
