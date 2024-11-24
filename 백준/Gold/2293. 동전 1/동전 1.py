import sys

input = lambda: sys.stdin.readline().rstrip()

N, T = map(int,input().split())
coins = []
answer =set()

for _ in range(N):
  coins.append(int(input()))

coins.sort()

dp = [0 for i in range(T + 1)]
dp[0] = 1

for coin in coins:
    for i in range(coin, T + 1): 
        dp[i] += dp[i - coin]

print(dp[T])