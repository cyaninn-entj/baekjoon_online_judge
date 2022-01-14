#https://www.acmicpc.net/problem/1157
usr_in=input().upper()
set_usr_in=list(set(usr_in))

cnt_ls=[0]*len(set_usr_in)
#print(cnt_ls)

for i, cht in enumerate(set_usr_in) :
    cnt_ls[i] = usr_in.count(cht)
    
if cnt_ls.count(max(cnt_ls)) == 1 :
    max_idx = cnt_ls.index(max(cnt_ls))
    print(set_usr_in[max_idx])
else : 
    print("?")
