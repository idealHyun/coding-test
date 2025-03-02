import sys
input = lambda: sys.stdin.readline().rstrip()

N,K =map(int,input().split())
bag=[]
for _ in range(N):
  bag.append(tuple(map(int,input().split())))

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for n in range(1,N+1):
  w,v = bag[n-1]
  for i in range(K+1):
    if i < w:
      dp[n][i] = dp[n-1][i]
    elif i >= w:
      dp[n][i] = max(dp[n-1][i-w]+v, dp[n-1][i])

print(dp[N][K])
