#https://www.acmicpc.net/problem/10250
import math

def assign(h, w, n) :
    height=h
    weith=w
    order=n
    floor,room_n = 0, 0
    
    if order <= height :
        floor=order
        room_n=1
    else :
        if order%height==0 :
            floor=height
        else :
            floor=order%height
        room_n=math.ceil(order/height)
        
    result=floor*100+room_n
    return result

_t=int(input())
roomnumber=[]
for i in range(0,_t) :
    h, w, n=input().split()
    H=int(h)
    W=int(w)
    N=int(n)
    fr=assign(H,W,N)
    roomnumber.append(fr)
    
for j in roomnumber :
    print(j)
