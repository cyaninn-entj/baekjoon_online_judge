#https://www.acmicpc.net/problem/10818
n=int(input())

num_ls=[]
for i in range(0,n) :
    num_ls.append(0)

num_ls=list(map(int, input().split()))
'''
num_ls.sort()

for i in range(0,n) :
    if i==0 :
        print(num_ls[0],end=" ")
    elif i==n-1 :
        print(num_ls[i],end=" ")
'''

print(min(num_ls),max(num_ls))
