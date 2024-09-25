# 입력 처리
import sys
N= int(sys.stdin.readline().rstrip())

arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

dp={}
dp[0]=[1,0]
dp[1]=[0,1]
dp[2]=[1,1]
dp[3]=[1,2]
for i in range(4,max(arr)+1):
    a,b=dp[i-1]
    c,d=dp[i-2]
    dp[i]=[a+c,b+d]

for i in arr:
    print(f'{dp[i][0]} {dp[i][1]}')
