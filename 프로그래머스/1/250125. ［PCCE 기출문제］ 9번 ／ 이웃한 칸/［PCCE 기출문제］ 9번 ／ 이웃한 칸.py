def solution(board, h, w):
    answer = 0
    board_len = len(board)
    
    # 상 우 하 좌
    dw=[0,1,0,-1]
    dh=[1,0,-1,0]
    color = board[h][w]
    
    for i in range(4):
        nh = h+dh[i]
        nw = w+dw[i]
        if  0<= nh <board_len and 0<= nw < board_len and board[nh][nw] == color:
            answer+=1
            
    return answer