#https://www.acmicpc.net/problem/10951
a=[]
b=[]

i=0
while True :
    try :
        a_in, b_in = map(int, input().split())
        a.append(a_in)
        b.append(b_in)

        if a_in==b_in==0 :
            break

        print(a[i]+b[i])
        i += 1
    except EOFError :
        break
