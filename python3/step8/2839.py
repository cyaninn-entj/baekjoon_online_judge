#https://www.acmicpc.net/problem/2839

#5로 나누어 떨어지는가? - 3 6 9 12 순으로 뺏을때 음수인가? - 3 6 9 12 순으로 뺏을때 5로 나눴을때 나누어 떨어지는가?

kg=int(input())
result=0

if kg%5==0 :
    result=int(kg/5)
    #print("kg%5==0")
else :
    for i in range(1,5) :
        if kg-3*i < 0 :
            result=-1
            break
        elif (kg-3*i)%5==0 :
            result= int((kg-3*i)/5) + i
            #print("(kg-3*i)%5==0")
            break
    if result==0 :
        result=-1

            
        
print(result)
