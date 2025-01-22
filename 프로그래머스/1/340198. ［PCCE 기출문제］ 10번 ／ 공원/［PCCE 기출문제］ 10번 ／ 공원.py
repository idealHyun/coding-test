def solution(mats, park):
    answer = 0
    w_length = len(park[0])
    h_length = len(park)
    
    def calculate_length(i,j):                
        visited = [[False for _ in range(w_length)] for _ in range(h_length)]
        min_length = 1
        visited[i][j] = True
        
        # 해당 변을 가진 정사각형에 다 -1 인지 확인
        def check(n,visited,i,j):
            for a in range(i,i+n):
                if a >= h_length:
                    return False
                for b in range(j,j+n):
                    if b>= w_length:
                        return False
                    if park[a][b] != "-1":
                        return False
                    
            return True
        
        while(check(min_length+1,visited,i,j)):
            min_length +=1
        
        return min_length
        
    # 각 위치에서 가장 큰 정사각형 변 길이 구하기
    for i in range(h_length):
        for j in range(w_length):
            if park[i][j] == "-1":
                min_length = calculate_length(i,j)
                if answer < min_length:
                    answer = min_length
    
    # 구한 값으로 mats 중 가장 큰 값, 돗자리 못깔면 -1
    filter_mats = [x for x in mats if x <= answer]
    
    if len(filter_mats)==0:
        return -1
    else:
        return max(filter_mats)
