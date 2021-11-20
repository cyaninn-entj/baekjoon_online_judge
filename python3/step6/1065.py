#https://www.acmicpc.net/problem/1065
def hansu(n) :
    if n<100 :
        return True
    elif n<1000 :
        one=n%10
        ten=(n%100)//10
        hund=n//100
        if hund-ten == ten-one :
            return True
        else :
            return False


def check(number) :
    cnt=0
    for i in range(1,number+1) :
        if hansu(i)==True :
            cnt=cnt+1
        else :
            cnt+=0
    return cnt

n_in=int(input())
print(check(n_in))