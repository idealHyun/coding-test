# https://www.acmicpc.net/problem/1446
import sys
input = lambda: sys.stdin.readline().rstrip()

N,D=map(int,input().split())
roads = []
dp=[i for i in range(D+1)]

# 필요없는 값 제거 (지름길이 더 걸릴 때, 지름길이 D 넘어갈 때)
for _ in range(N):
  s,e,v = map(int,input().split())
  if not e-s < v and e <= D:
    roads.append((s,e,v))

roads.sort(key=lambda x:x[0])

for i in range(D+1):
  if i>0:
    dp[i]=min(dp[i-1]+1,dp[i])

  for road in roads:
    s,e,v = road
    if s>i:
      break

    if s==i and dp[e]>dp[i] + v:
      dp[e]=dp[i] + v

print(dp[D])
