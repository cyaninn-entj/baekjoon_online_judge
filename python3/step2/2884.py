#https://www.acmicpc.net/problem/2884
hour, minute = map(int, input().split())

if minute>=45 :
    minute=minute-45
else :
    minute=minute+60-45
    if hour==0 :
        hour=23
    else :
        hour=hour-1
print(hour,minute)
