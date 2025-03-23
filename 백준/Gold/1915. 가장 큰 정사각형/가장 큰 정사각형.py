import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]
dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
answer = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if matrix[i - 1][j - 1] == 1:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            answer = max(answer, dp[i][j])

print(answer ** 2)
