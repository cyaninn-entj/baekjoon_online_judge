#https://www.acmicpc.net/problem/8958
test_num=int(input())
pr_result=[]

for i in range(0,test_num) :
    ox=str(input())
    result=[]

    for k in range(0,len(ox)) :
        result.append(0)

    if ox[0]=='O' :
            result[0]=1
    
    for j in range(1,len(ox)) :
        if ox[j]=='O' :
            if ox[j-1]=='O' :
                result[j]=result[j-1]+1
            elif ox[j-1]=='X' :
                result[j]=1
        elif ox[j]=='X' :
            result[j]=0
    pr_result.append(result)
    #print(result)

for i in range(0, len(pr_result)) :
    print(sum(pr_result[i]))