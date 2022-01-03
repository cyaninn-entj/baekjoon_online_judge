#https://www.acmicpc.net/problem/1157
usr_in=input()
up_usr_in=usr_in.upper()
set_usr_in=set(up_usr_in)

count_ls=[]
setusrin_countls=[]
for i in up_usr_in :
    count_ls.append(up_usr_in.count(i))

for j in set_usr_in :
    setusrin_countls.append(up_usr_in.count(j))

if setusrin_countls.count(max(setusrin_countls))>1 :
    print('?')
else :
    result=up_usr_in[count_ls.index(max(count_ls))]
    print(result)
