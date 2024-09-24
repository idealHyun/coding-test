# 입력 처리
import sys
N,M= map(int,sys.stdin.readline().rstrip().split())

dict={}

for i in range(N):
    name=sys.stdin.readline().rstrip()
    dict[name]=True

arr=[]
for _ in range(M):
    value=sys.stdin.readline().strip()
    if value in dict.keys():
        arr.append(value)

arr.sort()

print(len(arr))
for name in arr:
    print(name)