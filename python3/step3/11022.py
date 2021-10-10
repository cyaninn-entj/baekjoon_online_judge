#https://www.acmicpc.net/problem/11022
n=int(input())

a=[]
b=[]
result=[]
for i in range(0,n) :
    a_in, b_in = map(int, input().split())
    a.append(a_in)
    b.append(b_in)
    result.append(a[i]+b[i])

for j in range(0,n) :
    print("Case #%d: %d + %d = %d" % (j+1,a[j], b[j], result[j]))
