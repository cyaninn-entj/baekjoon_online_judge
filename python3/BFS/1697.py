#https://www.acmicpc.net/problem/1697

from collections import deque


def hind_and_seek(x,y) :
    need_visit=deque()
    visited=set()
    result=0

    if x>=y :
        result=x-y
        return result

    need_visit.append(x)
    sec=0
    while need_visit :
        sec+=1
        _floor=len(need_visit)
    
        for i in range(_floor) :
            current_node=need_visit[0]

            if current_node-1 not in visited and current_node-1>=0 :
                need_visit.append(current_node-1)
                visited.add(current_node-1)
            if current_node+1 not in visited and current_node+1<100001 :
                need_visit.append(current_node+1)
                visited.add(current_node+1)
            if current_node*2 not in visited and current_node*2<100001 :
                need_visit.append(current_node*2)
                visited.add(current_node*2)
            
            visited.add(current_node)

            if y in visited :
                #sec-=1
                result=sec
                need_visit.clear()
                break
            need_visit.popleft()
            
            #print(need_visit,sec)
            #print('-')
        
    return result

s_lo, bro_lo=map(int, input().split())
print(hind_and_seek(s_lo,bro_lo))
