import sys
n=int(sys.stdin.readline().rstrip())

arr=[]
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip().split())))

dp=[[0 for _ in range(i)] for i in range(1,n+1)]

dp[0]=arr[0]
if n>1:
    dp[1]=[arr[0][0]+arr[1][0],arr[0][0]+arr[1][1]]

for i in range(2,n):
    for j in range(len(dp[i])):
        if j==0:
            dp[i][j]=dp[i-1][j]+arr[i][j]
        elif j==len(dp[i])-1:
            dp[i][j]=dp[i-1][j-1]+arr[i][j]
        else:
            dp[i][j]=arr[i][j]+ max(dp[i-1][j],dp[i-1][j-1])

print(max(dp[n-1]))