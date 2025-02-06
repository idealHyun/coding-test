from collections import defaultdict, deque
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
tree_dict = defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree_dict[a].append(b)
    tree_dict[b].append(a)

parent = [0] * (N + 1) 
visited = [False] * (N + 1)

queue = deque([1])
visited[1] = True

while queue:
    node = queue.popleft()
    for child in tree_dict[node]:
        if not visited[child]: 
            visited[child] = True
            parent[child] = node
            queue.append(child)

for i in range(2, N + 1):
    print(parent[i])