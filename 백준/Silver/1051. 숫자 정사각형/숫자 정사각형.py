import sys
input=lambda: sys.stdin.readline().strip()

N,M=map(int,input().split())

rect=[]

for _ in range(N):
    rect.append(list(map(int,input())))

max_len = M if N>M else N
max_value=1

dx=[0,1,1]
dy=[1,0,1]

for y in range(N):
    for x in range(M):
        value=rect[y][x]
        # 정사각형의 변 길이
        for i in range(max_len,0,-1):
            if y+(i-1)<N and x+(i-1)<M:
                count=0
                for n in range(3):
                    ny=y+dy[n] * (i-1)
                    nx=x+dx[n] * (i-1)
                    if value!=rect[ny][nx]:
                        break
                    else:
                        count+=1
                        if count==3 and max_value<i:
                            max_value=i

print(max_value**2)