# 입력 처리
import sys
N= int(sys.stdin.readline().rstrip())

arr=[]
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort(reverse=True)

sum=-1

for i in range(N-2):
    if arr[i]<arr[i+1]+arr[i+2]:
        sum=arr[i]+arr[i+1]+arr[i+2]
        break

print(sum)