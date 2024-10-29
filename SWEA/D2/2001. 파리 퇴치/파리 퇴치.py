T = int(input())

for test_case in range(1,T+1):
    N,M = map(int,input().split())

    maxtrix = []
    max_count=0
    
    for _ in range(N):
        maxtrix.append(list(map(int,input().split())))

    def func(y,x):
        count = 0
        for i in range(M):
            for j in range(M):
                count +=maxtrix[x+i][y+j]
            
        return count

    for i in range(N-M+1):
        for j in range(N-M+1):
            count = func(i,j)
            if max_count<count:
                max_count=count

    print(f'#{test_case} {max_count}')