### 입력 처리
# 정점의 개수 N(1 ≤ N ≤ 1,000)
# 간선의 개수 M(1 ≤ M ≤ 10,000)
# 탐색을 시작할 정점의 번호 V
# 어떤 두 정점 사이에 여러 개의 간선
N,M,V = list(map(int,input().split()))

### 문제 풀이
from collections import defaultdict

graph=defaultdict(list)

# 그래프 초기화
for i in range(1,N+1):
    graph[i]

# 그래프 연결
for _ in range(M):
    start,end = list(map(int,input().split()))
    graph[start].append(end)
    graph[end].append(start)

# 그래프 정렬
for key in graph.keys():
    graph[key].sort()

# DFS
visited = [False] * N

def dfs(n):
    if visited[n-1]==False:
        visited[n-1]=True
        print(n,end=" ")
        for v in graph[n]:
            dfs(v)

dfs(V)

print()

# BFS
from collections import deque
visited = [False] * N

def bfs(n):
    q=deque()
    q.append(n)

    while q:
        v=q.popleft()
        if visited[v-1]==False:
            visited[v-1]=True
            q.append(v)
            print(v,end=" ")
            for k in graph[v]:
                q.append(k)

bfs(V)