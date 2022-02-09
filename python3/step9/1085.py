#https://www.acmicpc.net/problem/1085

x,y,w,h=map(int, input().split())
len_ls=[]
len_ls.append(x)
len_ls.append(y)
len_ls.append(w-x)
len_ls.append(h-y)
len_ls.sort()
#print(len_ls)
print(len_ls[0])
