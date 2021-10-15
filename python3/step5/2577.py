#https://www.acmicpc.net/problem/2577
a=int(input())
b=int(input())
c=int(input())

g=a*b*c
fn=[]
num_pr=[0]*10

for i in range(0,9) :
    fn_in=(g%10**(i+1)) // 10**i
    fn.append(fn_in)
    for j in range(0,10) :
        if fn[i]==j :
            num_pr[j]=num_pr[j]+1

if fn[8]==0 :
    if fn[7]==0:
        num_pr[0]=num_pr[0]-2
    else :
        num_pr[0]=num_pr[0]-1


for i in range(0,10) :
    print(num_pr[i])

#print(fn)