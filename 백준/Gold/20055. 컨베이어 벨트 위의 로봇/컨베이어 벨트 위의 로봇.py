import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robot_position = deque([False] * N)  
answer = 1

while True:
    # 벨트와 로봇을 한 칸 회전
    belt.rotate(1)
    robot_position.rotate(1)
    # 회전 후, 로봇 내리기
    robot_position[-1] = False

    # 가장 먼저 올라온 로봇부터 이동할 수 있으면 이동한다.
    for i in range(N-2, -1, -1):
        # 로봇 존재해야하고, 다음 칸에 로봇 없어야되고, 내구도 0 이상
        if robot_position[i] and not robot_position[i+1] and belt[i+1] > 0:
            # 로봇 이동
            robot_position[i] = False
            robot_position[i+1] = True
            belt[i+1] -= 1 
    # 이동 후에도 내리는 위치(N-1)에 로봇이 있으면 내려주기
    robot_position[-1] = False

    # 올리는 위치에 로봇이 없고 내구도가 0 이상
    if belt[0] > 0 and not robot_position[0]:
        robot_position[0] = True
        belt[0] -= 1

    # 내구도가 0인 칸의 개수가 K개 이상이면 종료
    if belt.count(0) >= K:
        print(answer)
        break

    answer += 1
