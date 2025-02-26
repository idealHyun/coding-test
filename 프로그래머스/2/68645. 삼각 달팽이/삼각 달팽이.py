def solution(n):
    answer = []
    inf = float('inf')

    matrix = []
    for i in range(1, n + 1):
        arr = [inf for _ in range(i)]
        matrix.append(arr)

    # 초기 상태 설정
    y, x, direction, num = 0, 0, 2, 1

    while num <= n * (n + 1) // 2:
        matrix[y][x] = num
        position = direction // 3

        # 배열 position값 채우기 (direction % 3 == 2)
        if direction % 3 == 2:
            dy = y + 1

            if dy < n and matrix[dy][position] == inf:
                y = dy
            else:
                x += 1
                direction += 1

        # 오른쪽으로 이동하며 값 채우기 (direction % 3 == 0)
        elif direction % 3 == 0:
            dx = x + 1

            if dx < len(matrix[y]) and matrix[y][dx] == inf:
                x = dx
            else:
                y -= 1
                x -= 1
                direction += 1

        # 왼쪽 대각선으로 올라가기
        # position - 곱한 위치에 값 넣기 (direction % 3 == 1)
        elif direction % 3 == 1:
            dy = y - 1
            dx = x-1

            if dy >= 0 and matrix[dy][dx] == inf:
                x -=1
                y-=1
            else:
                y += 1
                direction += 1

        num += 1

    return sum(matrix,[])
