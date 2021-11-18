#https://www.acmicpc.net/problem/4673
def selfnumber(number) :
    selfN=0
    check=0
    for thousand in range(0,10) :
        for hundread in range(0,10) :
            for ten in range(0,10) :
                for one in range(0,10) :
                    if number==(1001*thousand)+(101*hundread)+(11*ten)+(2*one) :
                        check=check+1
                    else :
                        check=check+0
    if check==0 :
        selfN=number
    return selfN

for i in range(1, 10001) :
    result=selfnumber(i)
    if result!=0 :
        print(result)




