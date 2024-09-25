# 입력 처리
import sys
N,M=map(int,sys.stdin.readline().rstrip().split())

arr=list(map(int,sys.stdin.readline().rstrip().split()))

sum_arr=[0] * (N+1)

for i in range(N):
    sum_arr[i+1]+=sum_arr[i]+arr[i]

for i in range(M):
    s,e=map(int,sys.stdin.readline().rstrip().split())

    print(sum_arr[e]-sum_arr[s-1])