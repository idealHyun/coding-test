# 입력 처리
import sys
sys.setrecursionlimit(10**6)
N,M = map(int,sys.stdin.readline().rstrip().split())

import itertools

arr=[i for i in range(1,N+1)]

combinations = itertools.combinations(arr,M)

for k in combinations:
    for i in k:
        print(i,end=" ")
    print()
