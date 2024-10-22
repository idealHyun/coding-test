import sys
input=lambda: sys.stdin.readline().strip()

N = int(input())

dp = [0] * (N+1)

dp[1]=1
if N>1:
    dp[2]=3
if N>2:
    dp[3]=5

for i in range(4,N+1):
    dp[i]=dp[i-1]%10007 +(dp[i-2]*2)%10007

print(dp[N]%10007)
