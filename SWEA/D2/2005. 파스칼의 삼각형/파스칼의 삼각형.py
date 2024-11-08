from collections import deque

T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    dp = [[1] * i for i in range(N+1)]

    if N>1:
        dp[1]=[1]
    if N>1:
        dp[2]=[1,1]

    for i in range(3,N+1):
        arr=[]
        for j in range(1,i-1):
            arr.append(dp[i-1][j-1]+dp[i-1][j])
            
        dp[i] = [1]+arr+[1]
    
    print(f'#{test_case}')
    for line in dp[1:]:
        for item in line:
            print(item, end=' ')
        print()
