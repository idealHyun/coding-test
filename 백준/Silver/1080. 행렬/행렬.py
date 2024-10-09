import sys
input=lambda: sys.stdin.readline().strip()

N,M=map(int,input().split())

before=[]
after=[]
change=[[False for _ in range(M)] for _ in range(N)]

for _ in range(N):
    before.append(list(map(int,input())))

for n in range(N):
    line = list(map(int,input()))
    for i,v in enumerate(line):
        if before[n][i] != v:
            change[n][i]=True
    after.append(line)

# 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.

flag=True
count=0

if N<3 or M<3:
    for line in change:
        if True in line:
            flag=False

else:
    for i in range(N-2):
        for j in range(M-2):
            if change[i][j]==True:
                count+=1
                for k in range(3):
                    for z in range(3):
                        change[i+k][j+z]= not change[i+k][j+z]

for line in change:
    if True in line:
        flag=False

if flag:
    print(count)
else:
    print(-1)