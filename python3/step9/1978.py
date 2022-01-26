#https://www.acmicpc.net/problem/1978

def pn(n) :
    if n==1 or n==0 :
        return 0
    prime=[2,3,5,7,11,13,17,19,23,29,31]
    cks=0
    for i in prime :
        if n==i :
            return 1
        elif n > i :
            if n%i==0 : return 0
            else : cks=1
        else : return 0
    return cks
    
t=int(input())
num=input().split()
_sum=0
for j in range(0, t) :
    _sum+=pn(int(num[j]))
print(_sum)
