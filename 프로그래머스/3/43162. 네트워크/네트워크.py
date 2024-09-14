def solution(n, computers):
    answer = 0
    visited = [];
    
    for i in range(n):
        visited.append(False);
    
    def dfs(n):
        # False 일때
        if not visited[n]:
            visited[n]=True
            for index,computer in enumerate(computers[n]):
                if(computer==1):
                    dfs(index)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer+=1
        
    return answer