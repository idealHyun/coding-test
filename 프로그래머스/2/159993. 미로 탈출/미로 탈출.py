from collections import deque

def solution(maps):
    answer = 0
    w_length = len(maps[0])
    h_length = len(maps)
    S_location = None
    L_location = None
    E_location = None
    
    for i in range(h_length):
        for j in range(w_length):
            if maps[i][j] == 'S':
                S_location = (i,j)
            elif maps[i][j] == 'L':
                L_location = (i,j)
            elif maps[i][j] == 'E':
                E_location = (i,j)
        
    
    # S->L 가는 최소 초 세기
    # L->E 가는 최소 초 세기
    
    L_visited= [[False for _ in range(w_length)] for _ in range(h_length)]
    E_visited= [[False for _ in range(w_length)] for _ in range(h_length)]
    
    # 상 우 하 좌
    dw = [0,1,0,-1]
    dh = [1,0,-1,0]
    
    # qs=deque()
    # qs.append((1,2,3))
    # print(qs)
    
    
    def bfs(start_location,end_location,visited):
        sh,sw = start_location
        eh,ew = end_location
        q=deque()
        q.append((sh,sw,0))
        while(q):
            mh,mw,d = q.popleft()
            for i in range(4):
                nh = mh + dh[i]
                nw = mw + dw[i]
                if 0<= nh < h_length and 0<= nw < w_length and maps[nh][nw] != 'X' and visited[nh][nw] ==False:
                    if nw == ew and nh ==eh:
                        return d+1
                    else:
                        q.append((nh,nw,d+1))
                        visited[nh][nw]=True
                    
    S_to_L = bfs(S_location,L_location,L_visited)
    L_to_E = bfs(L_location,E_location,E_visited)
    
    if S_to_L and L_to_E:
        return S_to_L + L_to_E
    else:
        return -1