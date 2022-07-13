#https://www.acmicpc.net/problem/17478
a='"재귀함수가 뭔가요?"'
b='"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
c='마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
d='그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
e='라고 답변하였지.'
f='"재귀함수는 자기 자신을 호출하는 함수라네"'

n=int(input())

def FN(num) :
    global a, b, c, d, e, f
    if 0<num :
        print(a)
        print(b)
        print(c)
        print(d)
        a="____"+a
        b="____"+b
        c="____"+c
        d="____"+d
        e="____"+e
        f="____"+f
        return FN(num=num-1)
    else :
        print(a)
        print(f)
        for j in range(0,n+1) :
            print(e[j*4:])
        return None

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
FN(n)
