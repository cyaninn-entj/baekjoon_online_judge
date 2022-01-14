#https://www.acmicpc.net/problem/2941

def cro_char(word) :
    cnt=0
    word=word+'a'
    for i in range(0, len(word)) :
        if len(word)==1 or len(word)==0 : 
            cnt=0
        else : 
            if word[i]=='c' and (word[i+1]=='=' or word[i+1]=='-') : #c=, c-
                cnt-=1
            elif word[i]=='d' and word[i+1]=='z' and word[i+2]=='=' : #dz=
                cnt-=2
            elif word[i]=='d' and word[i+1]=='-' : #d-
                cnt-=1
            elif word[i]=='l' and word[i+1]=='j' : #lj
                cnt-=1
            elif word[i]=='n' and word[i+1]=='j' : #nj
                cnt-=1
            elif word[i]=='s' and word[i+1]=='=' : #s=
                cnt-=1
            elif word[i]=='z' and word[i+1]=='=' : #z=
                if word[i-1] != 'd' :
                    cnt-=1
                else : 
                    pass
            else : 
                pass

    cnt+=len(word) -1
    #print('len(word) : ',len(word))
    return cnt

usr_in=input()
result=cro_char(usr_in)
print(result)
