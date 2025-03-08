import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
num_arr = [int(input()) for _ in range(N)]
answer = 0

# 배열 내림차순 정렬
num_arr.sort(reverse=True)

# 0 이하 숫자의 첫 번째 인덱스 찾기
split_index = N
for i in range(N):
  if num_arr[i] <=0:
    split_index = i
    break

# 양수 배열과 음수 + 0 배열 분리
plus_arr = num_arr[0:split_index]
minus_arr = sorted(num_arr[split_index:])

# 양수 배열에서 1이 있는 경우 처리
# 1은 양수랑 곱하는 것보다 더하는게 결과값 최대화
if 1 in plus_arr:
  one_index = num_arr.index(1)
  one_arr = plus_arr[one_index:]
  plus_arr = plus_arr[:one_index]
  # 1의 개수 만큼 미리 결과 값에 더하기
  answer += len(one_arr)  

def sum_arr(arr):
  len_arr = len(arr)
  total = 0
  # 앞에서 부터 2개씩 묶어서 더하기
  for i in range(0,len_arr-1,2):
    total += arr[i] * arr[i+1]
  # 1개 남았을 경우 더하기
  if len_arr % 2 ==1 :
    total += arr[len_arr-1]

  return total

print(answer + sum_arr(plus_arr) + sum_arr(minus_arr))