# 입력 처리
import sys
N=int(sys.stdin.readline().rstrip())

from collections import deque

for _ in range(N):
    length=int(sys.stdin.readline().rstrip())
    s_x,s_y=map(int,sys.stdin.readline().rstrip().split())
    e_x,e_y=map(int,sys.stdin.readline().rstrip().split())
    visited=[[0 for _ in range(length)] for _ in range(length)]

    # 오른쪽 위 대각선부터 왼쪽 위 대각선까지 8방향
    dx=[1,2,2,1,-1,-2,-2,-1]
    dy=[2,1,-1,-2,-2,-1,1,2]

    def bfs(s_x,s_y):
        q=deque()
        q.append([s_x,s_y])

        while q:
            x,y=q.popleft()

            for i in range(8):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx>=0 and nx<length and ny>=0 and ny<length:
                    if visited[y][x]+1 < visited[ny][nx] or visited[ny][nx]==0:
                        visited[ny][nx]=visited[y][x]+1
                        q.append([nx,ny])
    if s_x==e_x and s_y ==e_y:
        print(0)
    else:
        bfs(s_x,s_y)
        print(visited[e_y][e_x])