import sys
input = lambda: sys.stdin.readline().rstrip()

M,N = map(int,input().split())
answer=[]

for i in range(M,N+1):
    if i==1:
        continue
    flag=True
    for j in range(2,int(i ** 0.5) + 1):
        if i%j==0:
            flag=False
            break
    if flag:
        print(i)  