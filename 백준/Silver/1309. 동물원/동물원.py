import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dp = [0 for _ in range(100001)]

dp[0]=1
dp[1]=3

for i in range(2,N+1):
  dp[i] = (2 * (dp[i-1] - dp[i-2]) % 9901 + dp[i-2] * 3 % 9901) % 9901

print(dp[N])