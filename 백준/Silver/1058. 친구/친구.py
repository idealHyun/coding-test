import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
f_matrix = [list(input()) for _ in range(N)]
answer = 0

for k in range(N):
  f_set= set([k])
  for i in range(N):
    if f_matrix[k][i]=='Y':
      f_set.add(i)
      for j in range(N):
        if f_matrix[i][j]=='Y':
          f_set.add(j)
  answer = max(answer,len(f_set))

print(answer-1)