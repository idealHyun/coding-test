import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
answer = [int(input()) for _ in range(N)]
count = 0
stack=[]
methods=[]
is_able=True

for n in answer:
  # n이 현재 넣은 최고 값보다 크면
  if n > count:
    while count < n:
      count +=1
      stack.append(count)
      methods.append('+')
    stack.pop()
    methods.append('-')
  else:
    if stack and n in stack:
      while True:
        c = stack.pop()
        methods.append('-')
        if c==n:
          break
    else:
      is_able=False
      break

if is_able:
  for m in methods:
    print(m)
else:
  print('NO')