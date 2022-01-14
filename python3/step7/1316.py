#https://www.acmicpc.net/problem/1316
def groupcheck(word) :
    group=0
    no_g=0
    if len(word) > 1 :
        for idx in range(0,len(word)-1) : 
            if word[idx] != word[idx+1] :
                new_word=word[idx+1:]
                if new_word.count(word[idx]) > 0 :
                    no_g=1
        if no_g == 0 :
            group=1
    else :
        if len(word)==1 :
            group=1
        else : 
            group=0
    return group

n=int(input())

result=0
for _ in range(n) :
    usr_in=""
    usr_in=input()
    result+=groupcheck(usr_in)

print(result)
