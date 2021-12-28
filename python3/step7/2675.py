#https://www.acmicpc.net/problem/2675

num=int(input())
str_ls=[]

for i in range(0,num) :
    usr_in=input()
    str_ls.append(usr_in)

#print(str_ls)


for j in range(0, num) :
    ls=str_ls[j]
    re_num=int(ls[0])
    re_str=ls[2:]
    for k in range(0, len(re_str)) :
        print(re_str[k]*re_num, end="")
    print("")
