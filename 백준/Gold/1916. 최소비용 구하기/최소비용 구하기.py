import sys
from collections import defaultdict
from heapq import heappop, heappush

input = lambda: sys.stdin.readline().rstrip()

N = int(input())  # 도시 개수
M = int(input())  # 버스 개수

inf = float('inf')
graph = defaultdict(list)
values = [inf] * N
visited = [False] * N  # 방문 체크 배열

for _ in range(M):
    s, e, v = map(int, input().split())
    graph[s].append((e, v))  # (도착지, 비용) 

start, end = map(int, input().split())

def dijkstra(start):
    hq = []
    values[start - 1] = 0  
    heappush(hq, (0, start))  # (거리, 시작점)

    while hq:
        current_dist, current_node = heappop(hq)

        if visited[current_node - 1]:  # 이미 방문한 노드면 무시
            continue

        visited[current_node - 1] = True  # 현재 노드를 방문 처리

        for next_node, weight in graph[current_node]:
            new_dist = current_dist + weight

            if new_dist < values[next_node - 1]:
                values[next_node - 1] = new_dist
                heappush(hq, (new_dist, next_node))

dijkstra(start)

print(values[end - 1])
