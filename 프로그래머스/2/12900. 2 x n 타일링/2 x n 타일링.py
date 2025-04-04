def solution(n):
    dp = [0] * (n+1)
    
    if n>0:
        dp[1]=1
    if n>2:
        dp[2]=2
    if n>3:
        dp[3]=3
        
    for i in range(4,n+1):
        dp[i]=dp[i-1]%1000000007+dp[i-2]%1000000007
        
    # print(dp)
    
    return dp[n]%1000000007