# 입력 처리
import sys
N, K = map(int, sys.stdin.readline().rstrip().split())

arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

count = 0
for i in range(N-1, -1, -1):
    if K >= arr[i]:
        count += K // arr[i] 
        K %= arr[i]  

print(count)