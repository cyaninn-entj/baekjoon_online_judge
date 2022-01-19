#https://www.acmicpc.net/problem/1712

'''
A+BX < CX
A < (C-B)X
A/(C-B) < X
'''
A,B,C=input().split()
A=int(A)
B=int(B)
C=int(C)

if B >= C :
    X=-1
else : 
    X=A/(C-B)+1
    
print(int(X))
