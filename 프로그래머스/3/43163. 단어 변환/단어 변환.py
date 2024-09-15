import collections

def solution(begin, target, words):
    candidate_n = []
    length=len(begin)
    
    visited_org= [False] * len(words)
    
    def bfs():
        q = collections.deque()
        q.append((begin,0,visited_org))
        
        while q:
            word,n,visited =q.popleft()
                
            if word==target:
                candidate_n.append(n)
                continue
            else :
                # words에서 단어 하나만 차이나는 것에 대한 인덱스를 찾기
                indexs=[]
                for i,v in enumerate(words):
                    count = sum(1 for a, b in zip(word,v) if a == b)
                    if(count==length-1):
                        indexs.append(i)               
                # visited 에서 해당 인덱스 값이 False 인지 확인, 인덱스 값 없으면 continue
                if len(indexs)>0:
                    for i,v in enumerate(indexs):
                        # False 이면 q에 추가하고 해당 인덱스에 True 넣기
                        if not visited[v]:
                            visited[v]=True
                            q.append((words[v],n+1,visited))
                else :
                    continue
        
    bfs()
    
    if len(candidate_n)>0:
        return min(candidate_n)
    else :
        return 0