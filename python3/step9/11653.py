#https://www.acmicpc.net/problem/11653
def pn(num) :
    f=0
    if num==1 : return f
    for j in range(2,num) :
        if j*j<=num :
            if num%j==0 : return f
    return num

def fz(num) :
    for i in pn_ls :
        v=int(num/i)
        if num%i==0 :
            ls.append(i)
            if v==1 :
                break
            else :
                #print("run fz")
                fz(v); break
        else : pass
    return ls

ls=[]
pn_ls=[]
ck_n=0
for i in range(2,4999999) :
    ck_n=int(pn(i))
    if ck_n != 0 : pn_ls.append(ck_n)
    else : pass


n=int(input())
if n==1 : pass
else :
    result=fz(n)
    for i in result :
        print(i)

#print(pn_ls)
