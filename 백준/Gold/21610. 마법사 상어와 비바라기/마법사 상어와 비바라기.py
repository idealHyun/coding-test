import sys
input = lambda: sys.stdin.readline().rstrip()

def move_cloud(cloud_positions,d,size):
  moved_cloud_positions=[]

  for cloud in cloud_positions:
    y,x = cloud
    # 행과 열 연결되있어서 % 연산 이용
    moved_cloud_positions.append(( (y+cloud_dy[d] * size)%N , (x+cloud_dx[d] * size)%N  ))

  return moved_cloud_positions

def rain(cloud_positions):
  for cloud in cloud_positions:
    y,x = cloud
    matrix[y][x] +=1

def check_diagonal_and_increment(cloud_positions):
  for cloud in cloud_positions:
    y,x = cloud
    # 미리 정의한 구름 이동 방향 이용
    for i in range(1,8,2):
      nx = x+cloud_dx[i]
      ny = y+cloud_dy[i]
      # 대각선 방향 확인은 N*N 격자에서만 확인
      if 0<= nx <N and 0<= ny <N and matrix[ny][nx]>0:
        matrix[y][x]+=1

def create_cloud(past_cloud_positions):
  past_cloud_positions_set = set(past_cloud_positions)
  new_cloud_positions=[]

  for i in range(N):
    for j in range(N):
      # 물의 양이 2이상이고, 이전에 구름이 존재하지 않았어야함
      if matrix[i][j] >=2 and (i,j) not in past_cloud_positions_set:
        new_cloud_positions.append((i,j))
        matrix[i][j] -=2

  return new_cloud_positions

N,M = map(int,input().split()) # 격자 사이즈 길이, 명령 개수
matrix = [list(map(int,input().split())) for _ in range(N)]
commands = [tuple(map(int,input().split())) for _ in range(M)]

# 구름 이동 방향 8개 방향
cloud_dx = [-1,-1,0,1, 1,1, 0,-1]
cloud_dy = [0,-1,-1,-1,0,1,1,1]

# 구름 좌표 - 처음 위치는 고정
cloud_positions= [(N-1,0),(N-1,1),(N-2,0),(N-2,1)] 

# 명령 수행
for command in commands:
  direction, size = command
  
  # 구름 좌표 이동
  cloud_positions = move_cloud(cloud_positions,direction-1,size)

  # 구름 비내리기
  rain(cloud_positions)

  # 대각선 물이 존재하는지 체크하고 물의 양 증가시키기
  check_diagonal_and_increment(cloud_positions)

  # 구름 생성
  cloud_positions = create_cloud(cloud_positions)

print(sum(sum(row) for row in matrix))