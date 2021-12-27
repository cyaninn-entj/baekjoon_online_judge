#https://www.acmicpc.net/problem/11720
lenth_in=int(input())
num_in=str(input())

sum=0
for i in range(0,lenth_in) :
    sum+=int(num_in[i])
    #print(num_in[i])

print(sum)
