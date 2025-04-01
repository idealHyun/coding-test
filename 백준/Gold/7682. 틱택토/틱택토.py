# https://www.acmicpc.net/problem/7682
import sys
input = lambda: sys.stdin.readline().rstrip()

def check_win(matrix, p):
    # 가로, 세로
    for i in range(3):
        if all(matrix[i][j] == p for j in range(3)):
            return True
        if all(matrix[j][i] == p for j in range(3)):
            return True
    # 대각선 2방향
    if all(matrix[i][i] == p for i in range(3)):
        return True
    if all(matrix[i][2 - i] == p for i in range(3)):
        return True
    return False

while True:
    line = input()
    if line == 'end':
        break

    x_arr = []
    o_arr = []
    matrix = [['' for _ in range(3)] for _ in range(3)]

    # X,O 위치 추가하기
    for i in range(3):
        for j in range(3):
            value = line[i * 3 + j]
            if value == 'X':
                matrix[i][j] = 'X'
                x_arr.append((i, j))
            elif value == 'O':
                matrix[i][j] = 'O'
                o_arr.append((i, j))
            else:
                matrix[i][j] = '.'

    x_count = len(x_arr)
    o_count = len(o_arr)

    x_win = check_win(matrix, 'X')
    o_win = check_win(matrix, 'O')

    valid = True

    # X는 O보다 많거나 같고, 최대 1개 더 많아야 함
    if not (x_count == o_count or x_count == o_count + 1):
        valid = False
    # 둘다 이길수가 없음
    elif x_win and o_win:
        valid = False
    # X가 이겼는데 X가 O보다 개수가 1개 많은 아닌 경우
    elif x_win and x_count != o_count + 1:
        valid = False
    # O가 이겼는데 개수가 같지 않은 경우
    elif o_win and x_count != o_count:
        valid = False
    # 아무도 안이겼는데 총합 개수가 9개 아닌 경우
    elif not x_win and not o_win and x_count + o_count != 9:
        valid = False

    if valid:
        print('valid')
    else:
        print('invalid')
