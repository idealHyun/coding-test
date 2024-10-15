import sys
input=lambda: sys.stdin.readline().strip()

from collections import deque
left_arr=deque(list(input()))
N = int(input())
right_arr=deque()

for _ in range(N):
    command = input().split()
    if command[0]=='L':
        if left_arr:
            right_arr.appendleft(left_arr.pop())
    elif command[0]=='D':
        if right_arr:
            left_arr.append(right_arr.popleft())
    elif command[0]=='B':
        if left_arr:
            left_arr.pop()
    elif command[0]=="P":
        left_arr.append(command[1])

print(('').join(left_arr+right_arr))
