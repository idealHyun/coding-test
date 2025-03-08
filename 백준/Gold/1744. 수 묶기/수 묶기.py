import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
num_arr = [int(input()) for _ in range(N)]
answer = 0

# 배열 정렬
num_arr.sort(reverse=True)
split_index = N

for i in range(N):
  if num_arr[i] <=0:
    split_index = i
    break

# 양수 
plus_arr = num_arr[0:split_index]
if 1 in plus_arr:
  one_index = num_arr.index(1)
  one_arr = plus_arr[one_index:]
  plus_arr = plus_arr[:one_index]
  answer += len(one_arr)  

minus_arr = sorted(num_arr[split_index:])

for i in range(len(plus_arr))[::2]:
  if i + 1 < len(plus_arr):
    answer += plus_arr[i] * plus_arr[i+1]
  else:
    answer +=plus_arr[i]

for i in range(len(minus_arr))[::2]:
  if i + 1 < len(minus_arr):
     answer += minus_arr[i] * minus_arr[i+1]
  else:
    answer +=minus_arr[i]

print(answer)