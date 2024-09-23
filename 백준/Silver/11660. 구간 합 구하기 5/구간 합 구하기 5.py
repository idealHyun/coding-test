import sys
# 입력 처리
N, M = list(map(int, sys.stdin.readline().strip().split()))

# 원본 2차원 배열
arr=[]
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

# 누적합 계산
for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = arr[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
# print(prefix_sum)

for _ in range(M):
    i, j, x, y = list(map(int, sys.stdin.readline().strip().split()))
    
    # 2차원 구간합 공식
    result = prefix_sum[x][y] - prefix_sum[i - 1][y] - prefix_sum[x][j - 1] + prefix_sum[i - 1][j - 1]
    print(result)
