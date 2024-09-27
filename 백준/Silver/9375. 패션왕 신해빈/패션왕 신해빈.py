# 입력 처리
import sys
sys.setrecursionlimit(10**6)
N=int(sys.stdin.readline().rstrip())

from collections import defaultdict

for _ in range(N):
    M=int(sys.stdin.readline().rstrip())
    dict=defaultdict(list)
    for _ in range(M):
        name,kind=sys.stdin.readline().rstrip().split()
        dict[kind].append(name)
    
    count =1
    
    for kind in dict.keys():
        count*=len(dict[kind])+1

    print(count-1)