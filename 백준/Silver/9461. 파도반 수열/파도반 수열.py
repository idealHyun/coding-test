import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
case=[]
for _ in range(N):
    case.append(int(input()))

dp = [0] * 101
dp[1]=1
dp[2]=1
dp[3]=1

for i in range(4,max(case)+1):
    dp[i] = dp[i-3]+dp[i-2]

for c in case:
    print(dp[c])

