# 입력 처리
import sys
sys.setrecursionlimit(10**6)
N,M = map(int,sys.stdin.readline().rstrip().split())

arr=[]
for _ in range(N):
    s = sys.stdin.readline().rstrip()
    line=[]
    for v in s:
        line.append(int(v))
    arr.append(line)

from collections import deque

visited=[[False for _ in range(M)] for _ in range(N)]
maps=[[1 for _ in range(M)] for _ in range(N)]

# 상,우,하,좌
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def bfs(x,y):
    q=deque()
    q.append([y,x])

    while q:
        a=q.popleft()
        for i in range(4):
            nx=a[1]+dx[i]
            ny=a[0]+dy[i]
            if nx>=0 and nx<M and ny>=0 and ny<N:
                if visited[ny][nx]==False and arr[ny][nx]==1:
                    visited[ny][nx]=True
                    q.append([ny,nx])
                    maps[ny][nx] = maps[a[0]][a[1]] +1
        
bfs(0,0)
        
print(maps[N-1][M-1])