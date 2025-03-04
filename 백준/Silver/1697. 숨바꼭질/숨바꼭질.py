import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

def bfs(n):
    q = deque()
    q.append((n, 0))
    visited = set()
    visited.add(n)

    while q:
        current_n, current_count = q.popleft()

        if current_n == K:
            return current_count

        for next_n in (current_n - 1, current_n + 1, current_n * 2):
            if 0 <= next_n <= 100000 and next_n not in visited:
                visited.add(next_n)
                q.append((next_n, current_count + 1))

if N == K:
    print(0)
else:
    print(bfs(N))
