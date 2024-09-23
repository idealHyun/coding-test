# 입력 처리
import sys

N,M= map(int,sys.stdin.readline().rstrip().split())
# N은 가로, M은 세로

box=[] # 박스
good_tomato=[] # 익은 토마토 위치
emptys=0

for m in range(M):
    line = list(map(int,sys.stdin.readline().rstrip().split()))
    box.append(line)
    indexs= [i for i,v in enumerate(line) if v==1]
    for i in indexs:
        good_tomato.append((m,i))
    empty = [i for i,v in enumerate(line) if v==-1]
    emptys += len(empty)

# print(good_tomato)

# 문제 풀이

from collections import deque

count=0 # 날짜
q1= deque()
for t in good_tomato:
    q1.append(t)

# 상,우,하,좌
dy=[-1,0,1,0]
dx=[0,1,0,-1]

# BFS
def bfs(q):
    while q:
        t = q.popleft()
        # print(t)
        y=t[0]
        x=t[1]
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if ny>=0 and ny<M and nx>=0 and nx<N:
                if box[ny][nx]==0:
                    box[ny][nx]=1
                    q1.append([ny,nx])
                    good_tomato.append((ny,nx))

# 날짜 구하기
while q1:
    q2 = q1.copy()
    q1.clear()
    bfs(q2)
    count+=1

if len(good_tomato) == N*M - emptys:
    print(count-1)
else:
    print(-1)
