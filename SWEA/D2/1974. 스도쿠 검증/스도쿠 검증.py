T = int(input())

for test_case in range(1,T+1):
    sdoqu = []
    for _ in range(9):
        sdoqu.append(list(map(int,input().split())))

    is_sdoqu=True

    # 가로 체크
    def check_column(n):
        nums = set()
        for j in range(9):
            if sdoqu[n][j] in nums:
                return False
            else :
                nums.add(sdoqu[n][j])
        else:
            return True

    for n in range(9):
        if not (check_column(n)):
            is_sdoqu=False
            break
            
    # 세로체크
    def check_column(n):
        nums = set()
        for j in range(9):
            if sdoqu[j][n] in nums:
                return False
            else :
                nums.add(sdoqu[j][n])
        else:
            return True

    if is_sdoqu:
        for i in range(9):
            if not (check_column(i)):
                is_sdoqu=False
                break
            
    # 3x3 체크
    def check_33(y,x):
        nums = set()
        for i in range(3):
            for j in range(3):
                if sdoqu[y+i][x+j] in nums:
                    return False
                else :
                    nums.add(sdoqu[y+i][x+j])
        else:
            return True

    if is_sdoqu:
        for k in [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]:
            y,x = k
            if not (check_33(y,x)):
                is_sdoqu=False
                break

    if is_sdoqu:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
    