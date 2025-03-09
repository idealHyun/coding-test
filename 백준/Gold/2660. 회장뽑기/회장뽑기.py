import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict, deque

# 입력 처리
N = int(input())
friend_dict = defaultdict(list)
score_arr = []

while True:
  a, b = map(int,input().split())
  if a== -1 and b== -1:
    break
  friend_dict[a].append(b)
  friend_dict[b].append(a)

def bfs(i,visited,depth):
  q=deque()
  q.append((i,depth))
  while q:
    n, d = q.popleft()
    visited.add(n)
    if len(visited)==N:
      return d
    
    for c in friend_dict[n]:
      if c not in visited:
        q.append((c,d+1))

for i in range(1,N+1):
  visited = set([i])
  score_arr.append(bfs(i,visited,0))

min_score = min(score_arr)
print(f'{min_score} {score_arr.count(min_score)}')
for i in range(1,N+1):
  if score_arr[i-1]==min_score:
    print(i,end=' ')