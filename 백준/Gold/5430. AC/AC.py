import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

T = int(input())  # 테스트 케이스의 개수

for _ in range(T):
    p = input()  # 수행할 함수 p
    n = int(input())  # 배열에 들어있는 수의 개수
    line = input().strip('[]')

    # 빈 배열 처리
    if line:
        arr = deque(map(int, line.split(',')))
    else:
        arr = deque()

    flag = True
    reverse_flag = False  # 배열이 뒤집혔는지 여부를 저장

    for function in p:
        if function == "R":
            reverse_flag = not reverse_flag  # 뒤집기 상태를 반전
        elif function == "D":
            if arr:
                if reverse_flag:
                    arr.pop()  # 뒤집힌 상태에서는 뒤에서 제거
                else:
                    arr.popleft()  # 정상 상태에서는 앞에서 제거
            else:
                print("error")
                flag = False
                break

    if flag:
        if reverse_flag:
            arr.reverse()  # 뒤집힌 상태이면 최종적으로 한 번 뒤집기
        print("[" + ",".join(map(str, arr)) + "]")