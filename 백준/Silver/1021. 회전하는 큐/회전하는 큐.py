import sys
input=lambda: sys.stdin.readline().strip()

# 큐의 크기 N과 뽑아내려고 하는 수의 개수 M
N,M = map(int,input().split())

from collections import deque

arr= deque(list(map(int,input().split())))

q=deque([i for i in range(1,N+1)])

answer=0

while arr:
    if arr[0]==q[0]:
        arr.popleft()
        q.popleft()
    else:
        index=q.index(arr[0])
        if len(q)-index > index:
            answer+=index
            for _ in range(index):
                q.append(q.popleft())
        else:
            answer+=len(q)-index
            for _ in range(len(q)-index):
                q.appendleft(q.pop())

print(answer)