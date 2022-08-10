from collections import deque

def dfs(input_arr) :
    visited=[0]
    need_visit=deque()
    need_visit.append(1) #시작노드 추가
    NOnodes=-1

    while need_visit :
        current_node=need_visit.pop() #탐색필요 노드리스트에서 pop해서 현재노드로 설정
        NOnodes+=1

        if current_node not in visited : #방문리스트에 현재노드가 있는지 확인
            visited.append(current_node)
            for i in input_arr :
                # 정방향
                if i[0]==current_node :
                    if (i[1] not in visited) and (i[1] not in need_visit) :
                        need_visit.append(i[1])
                # 역방향         
                elif i[1]==current_node : 
                    if (i[0] not in visited) and (i[0] not in need_visit):
                        need_visit.append(i[0])
                #print(current_node,need_visit)
    return NOnodes

comnum=int(input())
NumOfCases=int(input())
arr=list()
for u in range(NumOfCases) :
    com = list(map(int,input().split()))
    arr.append(com)

result=dfs(arr)
print(result)
