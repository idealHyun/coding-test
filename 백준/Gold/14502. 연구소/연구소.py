import sys
input = lambda: sys.stdin.readline().rstrip()

# 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
N,M = map(int, input().split())

# 0은 빈 칸, 1은 벽, 2는 바이러스
# 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수

# 상,우,하,좌
dn=[1,0,-1,0]
dm=[0,1,0,-1]

from collections import deque
import copy

maps=[]
virus=deque()
answer=0

for n in range(N):
    line=list(map(int, input().split()))
    maps.append(line)
    for m in range(len(line)):
        if line[m]==2:
            virus.append((n,m))

# 바이러스 감염
def infect(): 
    copy_map=copy.deepcopy(maps)
    virus_copy = deque(virus)  # virus 리스트를 복사
    while virus_copy:
        n, m = virus_copy.popleft()
        for i in range(4):
            nn = n + dn[i]
            nm = m + dm[i]
            if 0 <= nn < N and 0 <= nm < M:
                if copy_map[nn][nm] == 0:
                    copy_map[nn][nm] = 2
                    virus_copy.append((nn, nm))
    
    count=0
    for line in copy_map:
        for value in line:
            if value==0:
                count+=1
    
    global answer

    answer=max(answer,count)

def wall(count):

    if count==3:
        infect()
        return
    
    for i in range(N):
        for j in range(M):
            if maps[i][j]==0:
                maps[i][j]=1
                wall(count+1)
                maps[i][j]=0

wall(0)

print(answer)