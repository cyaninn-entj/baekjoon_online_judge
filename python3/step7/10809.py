#https://www.acmicpc.net/problem/10809
s=input()
s_len=len(s)


for i in range(97, 123) :
    check=0
    for j in range(0,s_len) :
        if chr(i)==s[j] :
            print(j,end=" ")
            check=1
            break
    if check!=1 :
        print(-1,end=" ")
