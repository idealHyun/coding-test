import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

stack=[]

for _ in range(N):
    N = int(input())
    if N==0:
        stack.pop()
    else:
        stack.append(N)

sum=0
for i in stack:
    sum+=i

print(sum)
