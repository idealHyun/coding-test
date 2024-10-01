import sys
input = lambda: sys.stdin.readline().rstrip()

# 큐의 크기 N , 뽑아내려고 하는 수의 개수 M
N,M = map(int, input().split())

from collections import deque

arr=deque([i for i in range(1,N+1)])
answer=[]

for _ in range(N):
    for _ in range(M-1):
        arr.append(arr.popleft())
    
    answer.append(arr.popleft())
    

print("<",end="")
print(", ".join(map(str,answer)),end="")
print(">",end="")