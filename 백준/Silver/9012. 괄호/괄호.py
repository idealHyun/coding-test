import sys
input = lambda: sys.stdin.readline().rstrip()


N = int(input())

for _ in range(N):
    stack=[]
    line = input()
    for c in line:
        stack.append(c)
        if len(stack)>1 and stack[-1]==")" and stack[-2]=="(":
            stack.pop()
            stack.pop()
    
    if len(stack)==0:
        print("YES")
    else:
        print("NO")
