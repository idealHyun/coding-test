# 입력 처리
import sys
N = int(sys.stdin.readline().rstrip())

arr=list(map(int,sys.stdin.readline().rstrip().split()))

sorted_arr=sorted(arr)

sum=0
min=0

for m in sorted_arr:
    min+=m
    sum+=min

print(sum)
