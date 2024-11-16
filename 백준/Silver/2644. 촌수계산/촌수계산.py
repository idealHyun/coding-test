import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

N=int(input())
p1, p2 = map(int,input().split())

K = int(input())

family = defaultdict(list)
visited = [False for _ in range(N)]

for _ in range(K):
  a, b = map(int,input().split())

  family[a].append(b)
  family[b].append(a)

flag=True

def dfs(p1,p2,answer):
  global flag

  if p1==p2:
    flag=False
    print(answer)
    return

  for i in family[p1]:
    if visited[i-1]==False:
      visited[i-1]=True
      dfs(i,p2,answer+1)

visited[p1-1]=True
dfs(p1,p2,0)

if flag==True:
  print(-1)