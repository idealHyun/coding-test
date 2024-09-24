# 입력 처리
import sys
M,N,H = map(int,sys.stdin.readline().rstrip().split())
# M은 가로, N은 세로, H는 높이

box=[]
good_tomatoes=[]
visited=[[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

for h in range(H):
    floor=[]
    for n in range(N):
        l=list(map(int,sys.stdin.readline().rstrip().split()))
        for m,v in enumerate(l):
            if v==1:
                good_tomatoes.append([h,n,m])
                visited[h][n][m]=True
            if v==-1:
                visited[h][n][m]=True
        floor.append(l)
    box.append(floor)

from collections import deque

q=deque()

for m in good_tomatoes:
    q.append(m)

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dm=[0,0,-1,1,0,0]
dn=[0,0,0,0,1,-1]
dh=[1,-1,0,0,0,0]

def bfs(q):
    d=1
    while q:
        t = q.popleft()
        for i in range(6):
            nh=t[0] + dh[i]
            nn=t[1]+dn[i]
            nm=t[2]+dm[i]
            if nm>=0 and nm<M and nn>=0 and nn<N and nh>=0 and nh<H:
                if visited[nh][nn][nm]==False and box[nh][nn][nm]==0:
                    visited[nh][nn][nm]=True
                    box[nh][nn][nm]=box[t[0]][t[1]][t[2]]+1
                    d=box[nh][nn][nm]
                    q.append([nh,nn,nm])
    return d

day=bfs(q)

flag=True

for floor in box:
    for row in floor:
        for element in row:
            if element==False:
                flag=False
                break

print(day-1) if flag else print(-1)