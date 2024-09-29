# 입력 처리
import sys
input = lambda: sys.stdin.readline().rstrip()
# V는 정점, E는 간선개수
V,E = map(int,input().split())
# S는 시작 정점
S=int(input())

from collections import defaultdict
from heapq import heappop,heappush

INF = float('inf')
graph=defaultdict(list)
values=[INF for _ in range(V)]

for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u].append([v,w])

def djk(start):
    values[start-1]=0
    hq=[]
    heappush(hq,(0,start))
    while hq:
        v,s = heappop(hq)
        if values[s-1]>v:
            values[s-1]=v
            continue
        for end,value in graph[s]:
            if values[end-1]>value+v:
                values[end-1]=value+v
                heappush(hq,(value+v,end))

djk(S)

for v in values:
    if v==INF:
        print("INF")
    else:
        print(v)