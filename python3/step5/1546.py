#https://www.acmicpc.net/problem/1546
sub_num=int(input())
score=list(map(int, input().split()))

max_score=max(score)

#print(score)
for i in range(0, sub_num) :
    new_score=score[i]/max_score*100
    score[i]=new_score

sum_score=0
for i in range(0, sub_num) :
    sum_score=sum_score+score[i]

print(sum_score/sub_num)
