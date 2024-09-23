# 입력 처리
import sys

N= int(sys.stdin.readline().rstrip())

# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.

scores=[0]*301 # 점수가 적혀있는 배열

for i in range(1,N+1):
    scores[i]=int(sys.stdin.readline().rstrip())

dp=[0] * 301 # 마지막 계단에 따른 최대값이 적힘

dp[1]=scores[1]
dp[2]=scores[1]+scores[2]
dp[3]=max(scores[1]+scores[3],scores[2]+scores[3])

for i in range(4,N+1):
    dp[i]=max(dp[i-3]+scores[i-1]+scores[i],dp[i-2]+scores[i])

print(dp[N])