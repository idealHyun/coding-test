import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())  # 도시 개수

dp=[0] * 1001

dp[1]=1
dp[2]=2
dp[3]=3

for i in range(4,N+1):
    dp[i]=dp[i-1]%10007+dp[i-2]%10007

print(dp[N]%10007)
