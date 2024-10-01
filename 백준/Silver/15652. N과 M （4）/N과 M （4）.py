import sys
input = lambda: sys.stdin.readline().rstrip()

# 입력 받기
N, M = map(int, input().split())

def backtracking(N, M, start, sequence):
    # 수열의 길이가 M이 되면 출력
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    # start부터 N까지의 숫자를 하나씩 선택
    for i in range(start, N + 1):
        sequence.append(i)  # 현재 숫자를 수열에 추가
        backtracking(N, M, i, sequence)  # 다음 단계로 재귀 호출
        sequence.pop()  # 백트래킹: 추가한 숫자를 다시 제거하여 이전 상태로 돌아감

# 백트래킹 함수 호출
backtracking(N, M, 1, [])
