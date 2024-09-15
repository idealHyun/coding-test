import collections

def solution(maps):
    candidate_dis=[] # 후보 값
    xs= len(maps[0])
    ys = len(maps)
    
    # 위, 왼, 아래, 오른
    dy=[1,0,-1,0]
    dx=[0,-1,0,1]

    def bfs(x,y,d):
        queue=collections.deque()
        queue.append((x,y,d))
        
        while queue:
            x,y,d = queue.popleft()
            
            if(y==ys-1 and x==xs-1):
                candidate_dis.append(d)
                continue
            else:
                for i in range(4):
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if nx>=0 and nx<xs and ny>=0 and ny<ys:
                        if(maps[ny][nx]==1):
                            maps[ny][nx]=0
                            queue.append((nx,ny,d+1))
                    
    bfs(0,0,1)
        
    if len(candidate_dis)>0:
        candidate_dis.sort()
        return candidate_dis[0]
    else:
        return -1