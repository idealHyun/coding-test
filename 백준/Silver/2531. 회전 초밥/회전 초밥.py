# https://www.acmicpc.net/problem/2531
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

N, d, k, c = map(int, input().split())
foods = [int(input()) for _ in range(N)]
window_dict = defaultdict(int)

# 초기 윈도우 세팅
for i in range(k):
  window_dict[foods[i]] += 1

# 쿠폰 초밥 포함 여부
if c not in window_dict:
  answer = len(window_dict) + 1
else:
  answer = len(window_dict)

#  돌리기 시작
for i in range(1, N):
  # 앞의 초밥 제거
  window_dict[foods[i - 1]] -= 1
  if window_dict[foods[i - 1]] == 0:
    del window_dict[foods[i - 1]]

  # 뒤의 초밥 추가
  window_dict[foods[(i + k - 1) % N]] += 1

  # 쿠폰 초밥 포함 여부 체크
  if c not in window_dict:
    current = len(window_dict) + 1
  else:
    current = len(window_dict)

  answer = max(answer, current)

print(answer)