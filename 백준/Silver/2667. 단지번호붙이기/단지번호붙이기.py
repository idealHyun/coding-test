import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
matrix = []
visited = [[False for _ in range(N)] for _ in range(N)]
danji = []

for _ in range(N):
    matrix.append(list(map(int, input())))

# 상, 우, 하, 좌
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append([y, x]) 
    visited[y][x] = True
    count = 1

    while q:
        a = q.popleft()
        for i in range(4):
            ny = a[0] + dy[i]
            nx = a[1] + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    if matrix[ny][nx] == 1:
                        count += 1
                        q.append([ny, nx])

    danji.append(count)

for i in range(N):
    for j in range(N):
        if not visited[i][j] and matrix[i][j] == 1:
            bfs(j, i) 
danji.sort()

print(len(danji))
for d in danji:
    print(d)
