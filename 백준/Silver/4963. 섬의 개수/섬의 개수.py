import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

while(True):
    w, h = map(int,input().split())
    if w==0 and h==0:
        break

    matrix=[]
    visited = [[False for _ in range(w)] for _ in range(h)]
    answer =0

    for _ in range(h):
        matrix.append(list(map(int,input().split())))

    # 상,우,하,좌, 대각오른쪽위, 대각오른쪽아래, 대각왼쪽아래, 대각왼쪽위
    dx=[0,1,0,-1,1,1,-1,-1]
    dy=[1,0,-1,0,1,-1,-1,1]

    def bfs(y,x):
        q = deque()
        q.append([y,x])

        while q:
            a = q.popleft()
            for i in range(8):
                nx = a[1]+dx[i]
                ny = a[0]+dy[i]
                if 0<= nx <w and 0<= ny < h:
                    if visited[ny][nx]==False and matrix[ny][nx]==1:
                        visited[ny][nx]=True
                        q.append([ny,nx])


    for i in range(h):
        for j in range(w):
            if visited[i][j]==False and matrix[i][j]==1:
                bfs(i,j)
                answer+=1

    print(answer)

