# 입력 처리
import sys
sys.setrecursionlimit(10**6)
N,M=map(int,sys.stdin.readline().rstrip().split())

from collections import defaultdict

dict=defaultdict(list)
visited=[False] * N
count=0

for _ in range(M):
    s,e=map(int,sys.stdin.readline().rstrip().split())
    dict[s].append(e)
    dict[e].append(s)

def dfs(n):
    visited[n-1]=True
    for i in dict[n]:
        if visited[i-1]==False:
            dfs(i)
    
for k in range(1,N+1):
    if visited[k-1]==False:
        dfs(k)
        count+=1

print(count)