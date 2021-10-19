#https://www.acmicpc.net/problem/4344
case=int(input())

sub_sum=0
result=[]
for i in range(0, case) :
    sub_score=[]
    case_avg=0
    sub_score=list(map(int, input().split()))
    #print(sub_score)

    sub_sum=0
    for j in range(1, len(sub_score)) :
        sub_sum=sub_sum+sub_score[j]
    
    case_avg=sub_sum/sub_score[0]
    #print(case_avg)
    count=0
    for k in range(1, len(sub_score)) :
        if sub_score[k]>case_avg :
            count=count+1
    result.append(count/sub_score[0]*100)
    #print(result)


for i in range(0, case) :
    a=round(result[i],3)
    print("{:.3f}%".format(a))
