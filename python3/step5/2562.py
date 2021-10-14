#https://www.acmicpc.net/problem/2562
num_ls=[]

for i in range(0, 9) :
    num_in=int(input())
    num_ls.append(num_in)

for i in range(0, 9) :
    if num_ls[i] == max(num_ls) :
        print(num_ls[i])
        print(i+1)
