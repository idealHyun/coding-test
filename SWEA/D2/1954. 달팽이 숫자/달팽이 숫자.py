T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    inf = float('inf')

    matrix = [[inf for _ in range(N)] for _ in range(N)]
    
    # 우,하,좌,상
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]

    def func(x,y,direction,n):
        if n>N*N:
            return
        
        matrix[y][x]=n

        ny=y+dy[direction%4]
        nx=x+dx[direction%4]
        

        if ny>=0 and ny<N and nx>=0 and nx<N: 
            if matrix[ny][nx]==inf:
                func(nx,ny,direction,n+1)
            else:
                direction+=1
                x+=dx[direction%4]
                y+=dy[direction%4]

                func(x,y,direction,n+1)
        else:
            direction+=1
            x+=dx[direction%4]
            y+=dy[direction%4]
            func(x,y,direction,n+1)

    func(0,0,0,1)

    
    print(f'#{test_case}')
    for line in matrix:
        print(' '.join(map(str,line)))