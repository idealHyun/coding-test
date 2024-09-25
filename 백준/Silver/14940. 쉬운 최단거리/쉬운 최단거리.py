# 입력 처리
import sys
N,M= map(int,sys.stdin.readline().rstrip().split())

arr=[]
s=[0,0]
flag=False
for n in range(N):
    l=list(map(int,sys.stdin.readline().rstrip().split()))
    arr.append(l)
    if not flag:
        for i,v in enumerate(l):
            if v==2:
                s=[n,i]
                flag=True

visited=[[False for _ in range(M)] for _ in range(N)]
maps=[[0 for _ in range(M)] for _ in range(N)]

from collections import deque

# 상,우,하,좌
dn=[1,0,-1,0]
dm=[0,1,0,-1]

def bfs(s):
    q=deque()
    q.append(s)
    maps[s[0]][s[1]]=0
    visited[s[0]][s[1]]=True
    while q:
        qn,qm=q.popleft()
        for i in range(4):
            nn=qn+dn[i]
            nm=qm+dm[i]
            if nn>=0 and nn<N and nm>=0 and nm<M:
                if visited[nn][nm] == False and arr[nn][nm]!=0:
                    visited[nn][nm]=True
                    q.append([nn,nm])
                    maps[nn][nm]+=maps[qn][qm]+1

bfs(s)

for n,line in enumerate(maps):
    for m,v in enumerate(line):
        if arr[n][m]==1 and maps[n][m]==0:
            maps[n][m]=-1
        
    print(' '.join(map(str,line)))