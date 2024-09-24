# 입력 처리
import sys
N,M= map(int,sys.stdin.readline().rstrip().split())

dict={}

for i in range(N):
    poketmon=sys.stdin.readline().rstrip()
    dict[poketmon]=i+1
    dict[i+1]=poketmon

for _ in range(M):
    value=sys.stdin.readline().strip()
    try:
        print(dict[int(value)])
    except:
        print(dict[value])