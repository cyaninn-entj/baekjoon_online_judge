#https://www.acmicpc.net/problem/1152
usr_in=input()
blank=0
word=0

for i in usr_in :
    if i==' ' :
        blank+=1
        
#print(blank)

if usr_in[0]==' ' :
    if usr_in[-1]==' ' :
        word=blank-1
    else :
        word=blank
else : 
    if usr_in[-1]==' ' :
        word=blank
    else :
        word=blank+1
        
print(word)
