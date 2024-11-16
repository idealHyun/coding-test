import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int,input().split())
s=[]

def dfs(n,m):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    for i in range(1,N+1):
        if i in s:
            continue
        s.append(i)
        dfs(i+1,m)
        s.pop()

dfs(1,M)

