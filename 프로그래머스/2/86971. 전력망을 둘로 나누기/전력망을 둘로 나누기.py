from collections import defaultdict,deque

def solution(n, wires):
    answer = n
        
    def bfs(k,wire_dict):
        q=deque()
        q.append(k)
        n_set = set()
        while q:
            a=q.popleft()
            n_set.add(a)
            for i in wire_dict[a]:
                if not i in n_set:
                    q.append(i)
            
        return len(n_set)
    
    
    for i in range(len(wires)):
        s,e = wires[i]
        temp_wires = wires[:i]+wires[i+1:]
        wire_dict=defaultdict(list)
        for wire in temp_wires:
            a,b = wire
            wire_dict[a].append(b)
            wire_dict[b].append(a)
        
        s_num = bfs(s,wire_dict)
        e_num = bfs(e,wire_dict)
        answer = min(answer,abs(s_num-e_num))
        
    return answer