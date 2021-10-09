count=int(input())

a=[]
b=[]
result=[]
for i in range(0, count) :
    a_input,b_input=map(int, input().split())
    a.append(a_input)
    b.append(b_input)
    result.append(a[i]+b[i])
    

for i in range(0, count) :
    print(result[i])
