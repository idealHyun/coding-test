import sys

input = lambda: sys.stdin.readline().rstrip()

S = input()
stack=[]
result=[]
flag=False

for s in S:
    if s=="<":
        for _ in range(len(stack)):
            c=stack.pop()
            result.append(c)
        result.append(s)
        flag=True
        continue
    elif s==">":
        result.append(s)
        flag=False
        continue
    elif flag==False and s==" ":
        # 스택 내용 거꾸로 넣기
        for _ in range(len(stack)):
            c=stack.pop()
            result.append(c)
        result.append(" ")
        continue

    if flag:
        result.append(s)
    else:
        stack.append(s)

for _ in range(len(stack)):
            c=stack.pop()
            result.append(c)

print("".join(result))