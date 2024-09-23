# 입력 처리
import sys

N= int(sys.stdin.readline().rstrip())

dp=[N] * (N+1)

dp[3]=1
if N>=5:
    dp[5]=1

for i in range(6,N+1):
    dp[i]=min(dp[i-5],dp[i-3]) +1
    
print(dp[N]) if dp[N]<N else print(-1)