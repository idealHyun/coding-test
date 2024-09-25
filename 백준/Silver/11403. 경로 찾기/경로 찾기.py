# 입력 처리
import sys
N=int(sys.stdin.readline().rstrip())

from collections import defaultdict
arr=defaultdict(list)
for n in range(N):
    l=list(map(int,sys.stdin.readline().rstrip().split()))
    for i,v in enumerate(l):
        if v==1:
            arr[n].append(i)

visited=[[0 for _ in range(N)] for _ in range(N)]

def dfs(s,e):
    visited[s][e]=1
    if e in arr.keys():
        for k in arr[e]:
            if visited[s][k]==0:
                dfs(s,k)

for i in arr.keys():
    for j in arr[i]:
        dfs(i,j)

for line in visited:        
    print(' '.join(map(str,line)))