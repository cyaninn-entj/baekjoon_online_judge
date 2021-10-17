#https://www.acmicpc.net/problem/3052
num=[0]*10
for i in range(0,10) :
    num[i]=int(input())

for i in range(0,10) :
    num_odd=num[i]%42
    num[i]=num_odd

set_num=list(set(num))
#print(set_num)
print(len(set_num))
