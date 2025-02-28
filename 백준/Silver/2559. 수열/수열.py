import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque 

N,K = map(int,input().split())
arr = list(map(int,input().split()))

dp = deque([0] * N)

dp[0]=arr[0]
for i in range(1,K):
  dp[i] = dp[i-1]+arr[i]

for i in range(K,N):
  dp[i] = arr[i]+dp[i-1]-arr[i-K]

for _ in range(1,K):
  dp.popleft()

print(max(dp))