# 입력 처리
import sys
N= int(sys.stdin.readline().rstrip())

# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

costs=[]
for _ in range(N):
    costs.append(list(map(int,sys.stdin.readline().rstrip().split())))

# 초기화
dp = [[0]*3 for _ in range(N)]

# 초기값
dp[0]=costs[0]

# 최소값 구하기
for i in range(1,N):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2]) + costs[i][0]
    dp[i][1]=min(dp[i-1][0],dp[i-1][2]) + costs[i][1]
    dp[i][2]=min(dp[i-1][0],dp[i-1][1]) + costs[i][2]

print(min(dp[N-1]))