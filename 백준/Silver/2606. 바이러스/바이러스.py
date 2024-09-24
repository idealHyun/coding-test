# 입력 처리
import sys
N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

from collections import defaultdict
dict=defaultdict(list)

for i in range(M):
    s,e=map(int,sys.stdin.readline().rstrip().split())
    dict[s].append(e)
    dict[e].append(s)

visited=[False] * N

def dfs(n):
    visited[n-1]=True
    for c in dict[n]:
        if not visited[c-1]:
            dfs(c)

dfs(1)

print(visited.count(True)-1)