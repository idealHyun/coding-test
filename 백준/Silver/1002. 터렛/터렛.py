import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

for i in range(N):
    x1,y1,r1,x2,y2,r2= map(int,input().split())

    if x1==x2 and y1==y2:
        if r1==r2: # 같은 원
            print(-1)
        else : # 같은 중심, 반지름 크기가 다른 원
            print(0) 
    else:
        d = ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5 # 원 중심 사이 거리

        if d==r1+r2: # 원끼리 외접
            print(1)
        elif d==abs(r1-r2): # 원끼리 내접
            print(1)
        elif abs(r2 - r1) < d < r1 + r2: # 교점 2개
            print(2)
        else:
            print(0)