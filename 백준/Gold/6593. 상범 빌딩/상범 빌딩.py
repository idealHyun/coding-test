import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

# 동,서,남,북,상,하
dx=[1,-1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,1,-1]

while True:
  L, R, C = map(int,input().split())
  if L==0:
    break
  
  start_position=None
  building=[[] for _ in range(L)]
  visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
  is_escapable= False

  # 입력 처리 및 위치 파악
  for l in range(L):
    floor = [list(input()) for _ in range(R)]
    for r in range(R):
      for c in range(C):
        if not start_position and floor[r][c]=='S':
          start_position = (l,r,c,0)

    input()
    building[l]=floor
  
  # BFS
  q=deque()
  q.append(start_position)
  while q:
    z,y,x, t = q.popleft()
    if building[z][y][x]=='E':
      is_escapable = True
      break
    else:
      for i in range(6):
        nz = z+dz[i]
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<= nz < L and 0<= ny < R and 0<= nx < C and building[nz][ny][nx] !='#' and visited[nz][ny][nx]==False:
          visited[nz][ny][nx]=True
          q.append((nz,ny,nx,t+1))

  if is_escapable:
    print(f'Escaped in {t} minute(s).')
  else:
    print('Trapped!')