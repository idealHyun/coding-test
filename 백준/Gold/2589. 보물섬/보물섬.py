import sys
input = lambda: sys.stdin.readline().rstrip()

N,M = map(int,input().split())

map=[]
lands=[]
count_map=[[0 for _ in range(M)] for _ in range(N)]
inf = float('inf')

for n in range(N):
    line = input()
    map.append(line)
    for m in range(M):
        if line[m]=="L":
            lands.append((n,m))
        else:
            count_map[n][m]=inf

from collections import deque
import copy

# 상,우,하,좌
dn=[1,0,-1,0]
dm=[0,1,0,-1]
max_value=0

def bfs(a,b):
    q=deque()
    q.append((a,b))
    map_copy=copy.deepcopy(count_map)
    map_copy[a][b]=1
    count=1

    while q:
        n,m = q.popleft()
        for i in range(4):
            nn=n+dn[i]
            nm=m+dm[i]
            if nn>=0 and nn<N and nm>=0 and nm<M:
                if map_copy[nn][nm]!=inf and map_copy[nn][nm]==0:
                    map_copy[nn][nm]=map_copy[n][m]+1
                    count=map_copy[n][m]+1
                    q.append((nn,nm))

    return count

while lands:
    n,m=lands.pop()
    value=bfs(n,m)
    if value>max_value:
        max_value=value

print(max_value-1)

