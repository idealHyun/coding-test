for test_case in range(1,11):
    N = int(input())
    answer =0
    
    matrix=[]
    for _ in range(8):
        matrix.append(list(input()))

    def check_word(input_string):
        global answer

        for i in range(N // 2):
            if not input_string[i] == input_string[-i-1]:
                break
        else:
            answer +=1

    # 가로
    for i in range(8):
        for j in range(8-N+1):
            check_word(''.join(matrix[i][j:j+N]))

    # 세로
    for i in range(8):
        for j in range(8-N+1):
            input_string = ''
            for k in range(N):
                input_string+=matrix[j+k][i]
            check_word(input_string)

    print(f'#{test_case} {answer}')