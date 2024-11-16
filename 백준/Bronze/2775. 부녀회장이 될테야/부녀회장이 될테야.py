import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())

    dp=[[0 for _ in range(15)] for _ in range(15)]

    for i in range(15):
        dp[0][i] = i

    for k in range(1,K+1):
        for n in range(N+1):
            total = 0
            for p in range(n+1):
                total+= dp[k-1][p]
            dp[k][n]= total
    
    print(dp[K][N])

