from collections import defaultdict

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
                
    def dfs(num):
        nonlocal visited
        for i,c in enumerate(computers[num]):
            if c==1 and visited[i]==False:
                visited[i]=True
                dfs(i)
        
    for i in range(n):
        if(visited[i]==False):
            visited[i]=True
            dfs(i)
            answer+=1
    
    return answer