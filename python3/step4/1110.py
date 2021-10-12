#https://www.acmicpc.net/problem/1110
n=int(input())

i=0
x=n
while True :
    if x>9 :
        x= ((x%10)*10) + (((x//10) + (x%10))%10)
    else :
        x= (x*10) + x

    i+=1
    if x==n :
        break

print(i)