# 입력 처리
N, M = list(map(int, input().split()))
# N : 행 개수
# M : 열 개수
arr=[]
for _ in range(N):
    arr.append(list(map(int, input().split())))

prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]

# 누적합 계산
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix_sum[i][j] = arr[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
# print(prefix_sum)

K = int(input())

for _ in range(K):
    i, j, x, y = list(map(int, input().split()))
    
    # 2차원 구간합 공식
    result = prefix_sum[x][y] - prefix_sum[i - 1][y] - prefix_sum[x][j - 1] + prefix_sum[i - 1][j - 1]
    print(result)
