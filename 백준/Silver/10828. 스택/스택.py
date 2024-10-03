import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

stack=[]

for _ in range(N):
    arr=list(input().split())
    if arr[0]=="push":
        stack.append(arr[1])
    elif arr[0]=="pop":
        if stack:
            num = stack.pop()
            print(num)
        else:
            print(-1)
    elif arr[0]=="size":
        print(len(stack))
    elif arr[0]=="empty":
        if stack:
            print(0)
        else:
            print(1)
    elif arr[0]=="top":
        if stack:
            n = len(stack)
            print(stack[n-1])
        else:
            print(-1)