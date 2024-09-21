# 입력 처리
N, M = list(map(int, input().split()))
# N : 노드의 개수 
# M : 거리를 알고 싶은 노드 쌍의 개수
graph = {}

# 그래프 초기화 및 연결
for _ in range(N-1):
    s, e, d = list(map(int, input().split()))
    
    # 양방향으로 그래프에 연결
    if s-1 not in graph:
        graph[s-1] = []
    if e-1 not in graph:
        graph[e-1] = []
    
    graph[s-1].append((e-1, d))
    graph[e-1].append((s-1, d))

# print(graph)
### 문제 풀이
def dfs(s, e, d, visited):
    visited[s] = True
    
    for neighbor, weight in graph.get(s, []):  # s와 연결된 이웃 노드와 가중치
        if not visited[neighbor]:
            if neighbor == e:
                print(d + weight)
                return
            else:
                dfs(neighbor, e, d + weight, visited)

# 거리 계산 요청 처리
for _ in range(M):
    s, e = list(map(int, input().split()))
    d = 0
    visited = [False] * N
    dfs(s-1, e-1, d, visited)
