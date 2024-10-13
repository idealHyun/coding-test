def solution(x, y, n):
    answer = 0
    inf=float('inf')
    
    dp=[inf]*(y+1)
    dp[x]=0
    if y>x+n:
        dp[x+n]=1
    if y>x*2:
        dp[x*2]=1
    if y>x*3:
        dp[x*3]=1
    
    if x==y:
        return 0
    
    for i in range(x+n,y+1):
        arr=[]
        if i-n>=x:
            arr.append(dp[i-n])
        if i%2==0 and i//2 >=x:
            arr.append(dp[i//2])
        if i%3==0 and i//3 >=x:
            arr.append(dp[i//3])
        
        dp[i]=min(arr)+1   
            
    if dp[y]==inf:
        return -1
    else:
        return dp[y]