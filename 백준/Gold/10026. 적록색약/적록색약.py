import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque 

N =int(input())
color_arr = []
for _ in range(N):
  color_arr.append(list(input()))

# 상 우 하 좌
dw = [0,1,0,-1]
dh = [1,0,-1,0]

# 적록색맹 아닌 사람
a_visited = [[False for _ in range(N)] for _ in range(N)]
a_count = 0

# 적록색맹인 사람
b_visited = [[False for _ in range(N)] for _ in range(N)]
b_count=0

def check_a(h,w,c):
  q=deque()
  q.append((h,w))
  while q:
    ph, pw = q.popleft()
    for i in range(4):
      nh = ph + dh[i]
      nw = pw + dw[i]
      if 0<= nh < N and 0 <= nw < N and not a_visited[nh][nw] and c == color_arr[nh][nw]:
        q.append((nh,nw))
        a_visited[nh][nw]= True

def check_b(h,w,c):
  q=deque()
  q.append((h,w))
  while q:
    ph, pw = q.popleft()
    for i in range(4):
      nh = ph + dh[i]
      nw = pw + dw[i]
      if 0<= nh < N and 0 <= nw < N and not b_visited[nh][nw]:
        if c == 'R' or c== 'G':
          if color_arr[nh][nw] == 'R' or color_arr[nh][nw] == 'G':
            q.append((nh,nw))
            b_visited[nh][nw]= True
        elif c == color_arr[nh][nw]:
          q.append((nh,nw))
          b_visited[nh][nw]= True
          

for i in range(N):
  for j in range(N):
    if not a_visited[i][j]:
      check_a(i,j,color_arr[i][j])
      a_count +=1
    if not b_visited[i][j]:
      check_b(i,j,color_arr[i][j])
      b_count +=1

print(a_count,b_count)