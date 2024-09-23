# 입력 처리
import sys

N= int(sys.stdin.readline().rstrip())

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
MAX=1000001

dp=[MAX] * (N+1)
dp[1]=0

if N>=2:
    dp[2]=1
if N>=3:
    dp[3]=1

for i in range(4,N+1):
    method1=MAX
    method2=MAX
    if i%3 == 0 :
        method1= dp[i//3]
    if i%2 == 0 :
        method2= dp[i//2]
    dp[i]=min(method1,method2,dp[i-1]) +1

print(dp[N])