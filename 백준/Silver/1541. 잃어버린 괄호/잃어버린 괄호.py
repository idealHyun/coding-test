# 입력 처리
import sys
sys.setrecursionlimit(10**6)
calc=sys.stdin.readline().rstrip()

from collections import deque

stack=deque()

s_i=0
flag=False
for i,v in enumerate(calc):
    if v=="+":
        stack.append(calc[s_i:i])
        if flag:
            stack.append("-")
        else:
            stack.append("+")
        s_i=i+1
    elif v=="-":
        stack.append(calc[s_i:i])
        stack.append("-")
        s_i=i+1
        flag=True
    if i==len(calc)-1:
        stack.append(calc[s_i:])

sum=int(stack.popleft())

while stack:
    c=stack.popleft()
    if c=='+':
        n=int(stack.popleft())
        sum+=n
    elif c=='-':
        n=int(stack.popleft())
        sum-=n
        
print(sum)