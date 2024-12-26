def solution(k, dungeons):
    global answer,visited
    answer = 0
    visited = [False for _ in range(len(dungeons))]
    backtracking(k,0,dungeons)
    
    return answer

def backtracking(k,count,dungeons):
    global answer

    if count>answer:
        answer=count
    
    for i in range(len(dungeons)):
        if not visited[i] and k>= dungeons[i][0]:
            visited[i]=True
            backtracking(k-dungeons[i][1],count+1,dungeons)
            visited[i]=False
