import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
max_answer = arr[:]
min_answer = arr[:]

for _ in range(1, N):
    temp = list(map(int, input().split()))

    prev_max = max_answer[:]
    prev_min = min_answer[:]

    max_answer = [
        temp[0] + max(prev_max[0], prev_max[1]),
        temp[1] + max(prev_max),
        temp[2] + max(prev_max[1], prev_max[2])
    ]

    min_answer = [
        temp[0] + min(prev_min[0], prev_min[1]),
        temp[1] + min(prev_min),
        temp[2] + min(prev_min[1], prev_min[2])
    ]

print(f'{max(max_answer)} {min(min_answer)}')
