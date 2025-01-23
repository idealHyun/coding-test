from collections import deque

def solution(land):
    w_len = len(land[0])
    h_len = len(land)
    visited = [[False for _ in range(w_len)] for _ in range(h_len)]
    land_dict = {col:0 for col in range(w_len)}
    
    # 상 우 하 좌
    dw = [0,1,0,-1]
    dh = [1,0,-1,0]
    
    def bfs(x,y):
        q=deque([])
        q.append((y,x))
        oil_value = 1
        col_set = set()
        col_set.add(x)
        
        while(q):
            h,w = q.popleft()
            for i in range(4):
                nw = w+dw[i]
                nh = h+dh[i]
                if 0 <= nw < w_len and 0<= nh < h_len:
                    if not visited[nh][nw]:
                        visited[nh][nw]=True
                        if land[nh][nw]==1:
                            q.append((nh,nw))
                            col_set.add(nw)
                            oil_value +=1
        
        for col in col_set:
            land_dict[col] += oil_value
                
    for w in range(w_len):
        for h in range(h_len):
            if not visited[h][w] :
                visited[h][w]=True
                if land[h][w]==1:
                    bfs(w,h)
    
    return max(land_dict.values())