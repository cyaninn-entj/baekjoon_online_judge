#https://www.acmicpc.net/problem/5622
def dial(num) : 
    if num>0 : 
        result1=num+1
    else : 
        result1=11
    return result1

def tonum(c) : 
    if ord(c)>=65 and 68>ord(c) : 
        result=2
    elif ord(c)>=68 and 71>ord(c) : 
        result=3
    elif ord(c)>=71 and 74>ord(c) : 
        result=4
    elif ord(c)>=74 and 77>ord(c) : 
        result=5
    elif ord(c)>=77 and 80>ord(c) : 
        result=6
    elif ord(c)>=80 and 84>ord(c) : 
        result=7
    elif ord(c)>=84 and 87>ord(c) : 
        result=8
    elif ord(c)>=87 and 91>ord(c): 
        result=9
    return result

grandma=input()
dialnum=[]
sum=0
for i in range(0,len(grandma)) : 
    dialnum.append(tonum(grandma[i]))
    #print(dialnum[i])
for j in range(0,len(dialnum)) : 
    sum+=dial(dialnum[j])
    
print(sum)
