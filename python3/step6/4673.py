#https://www.acmicpc.net/problem/4673
generated_num=[]

def check_selfnum(number) :
    if number not in generated_num :
        return True
    else :
         return False
    
for i in range(1,10001) :
    for j in str(i) :
        i += int(j)
    generated_num.append(i)

for i in range(1,10001) :
    if check_selfnum(i)==True :
        print(i)




