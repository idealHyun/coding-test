import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input()) 

dp=[0] * (N+1)

dp[1]=0
if N>1:
    dp[2]=1
if N>2:
    dp[3]=1

for i in range(4,N+1):
    if i%3==0 and i%2==0:
        dp[i]=min(dp[i//3],dp[i//2],dp[i-1])+1
    elif i%3==0:
        dp[i]=min(dp[i//3],dp[i-1])+1
    elif i%2==0:
        dp[i]=min(dp[i//2],dp[i-1])+1
    else:
        dp[i]=dp[i-1]+1

print(dp[N])
print(N,end=" ")
num=N
while N!=1:
    if N%3==0 and N%2==0:
        a=dp[N//3]
        b=dp[N//2]
        c=dp[N-1]
        min_dp=min(dp[N//3],dp[N//2],dp[N-1])
        if min_dp==a:
            N=N//3
        elif min_dp==b:
            N=N//2
        else:
            N=N-1
    elif N%3==0:
        a=dp[N//3]
        c=dp[N-1]
        min_dp=min(dp[N//3],dp[N-1])
        if min_dp==a:
            N=N//3
        else:
            N=N-1
    elif N%2==0:
        b=dp[N//2]
        c=dp[N-1]
        min_dp=min(dp[N//2],dp[N-1])
        if min_dp==b:
            N=N//2
        else:
            N=N-1
    else:
        min_dp=dp[N-1]+1
        N=N-1
    print(N,end=" ")