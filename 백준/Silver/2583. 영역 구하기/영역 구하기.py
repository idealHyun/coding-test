# https://www.acmicpc.net/problem/2583
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

M,N,K = map(int,input().split())
visited = [[False for _ in range(N)] for _ in range(M)]
answer=[]

# 상 우 하 좌
dy = [1,0,-1,0]
dx = [0,1,0,-1]

for _ in range(K):
  min_x,min_y,max_x,max_y = map(int,input().split())
  for i in range(min_y,max_y):
    for j in range(min_x,max_x):
      visited[i][j]=True

def bfs(y,x):
  k=1
  q=deque()
  q.append((y,x))
  visited[y][x]=True
  while q:
    my,mx = q.popleft()
    for i in range(4):
      ny = my+dy[i]
      nx = mx+dx[i]
      if 0<= ny < M and 0<= nx < N and visited[ny][nx]==False:
        visited[ny][nx]=True
        q.append((ny,nx))
        k+=1
  answer.append(k)

for i in range(M):
  for j in range(N):
    if not visited[i][j]:
      bfs(i,j)

print(len(answer))
answer.sort()
print(*answer)