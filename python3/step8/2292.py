#https://www.acmicpc.net/problem/2292
'''
1그룹 6*0 + 1
2그룹 6*1 + 1
3그룹 6*3 + 1
4그룹 6*6 + 1
5그룹 6*10 + 1
'''

X=int(input())

i=0
j=0
while True :
    if X <= (6*i)+1 :
        print(j+1)
        break;
    else :
        j+=1
        i+=j
