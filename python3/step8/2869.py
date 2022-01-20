#https://www.acmicpc.net/problem/2869
import math

a,b,v=input().split()
A=int(a)
B=int(b)
V=int(v)

day=math.ceil( (V-A)/(A-B) +1 )

#print(A, B ,V)
print(day)
